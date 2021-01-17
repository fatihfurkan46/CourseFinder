from flask import Blueprint, redirect, url_for, render_template, flash, g
from flask_login import current_user, login_required

from app import db
from app.models.exam import Exam
from app.models.course import Course
from app.models.student import Student, association
from app.forms.course import CourseCreateForm, CourseEditForm, ExamCreateForm

course = Blueprint('course', __name__, url_prefix='/course')

@course.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('course.teacher_index'))
    else:
        return redirect(url_for('main.index'))


@course.route('/teacher/index')
@login_required
def teacher_index():
    courses = Course.query.filter_by(teacher=current_user)
    return render_template('views/course/teacher_index.html', title='My Courses', courses=courses)

@course.route('/teacher/create', methods=['GET', 'POST'])
@login_required
def teacher_create():
    form = CourseCreateForm()

    if form.validate_on_submit():
        course = Course()
        course.name = form.name.data
        course.grade_level = form.grade_level.data
        course.price = form.price.data
        course.teacher = current_user

        db.session.add(course)
        db.session.commit()

        return redirect(url_for('course.teacher_show', id=course.id))

    return render_template('views/course/teacher_create.html', title='Create Course', form=form)

@course.route('teacher/<int:id>')
@login_required
def teacher_show(id):
    course = Course.query.filter_by(id=id).first_or_404()
    exams = Exam.query.filter_by(course_id = course.id)
    return render_template('views/course/teacher_show.html', title='Show Course', course=course, exams=exams)

@course.route('teacher/<int:id>/edit', methods=['GET','POST'])
@login_required
def teacher_edit(id):
    course = Course.query.filter_by(id=id).first_or_404()
    form = CourseEditForm()

    if form.validate_on_submit():
        course.name = form.name.data
        course.grade_level = form.grade_level.data
        db.session.commit()

        flash('Course Update  Successfully', 'success')

    form.name.data = course.name
    form.grade_level.data = course.grade_level
    form.price.data = course.price

    return render_template('views/course/teacher_create.html', title='Edit Course', form=form)

@course.route('teacher/<int:id>/delete', methods=['GET','POST'])
@login_required
def teacher_delete(id):
    course = Course.query.filter_by(id=id).first()
    course.students = []
    for i in course.exams:
        Exam.query.filter_by(id=i.id).delete()
    db.session.delete(course)
    db.session.commit()
    flash('Course Delete Successfully', 'success')

    return redirect(url_for('course.teacher_index'))

@course.route('/teacher/<int:id>/add_exam', methods=['GET', 'POST'])
@login_required
def teacher_add_exam(id):
    form = ExamCreateForm()

    if form.validate_on_submit():
        exam = Exam()
        exam.name = form.name.data
        exam.date = form.date.data
        exam.course_id = id
        db.session.add(exam)
        db.session.commit()

        flash('Exam Add Successfully', 'success')

    return render_template('views/course/teacher_exam_add.html', title='Add Exam', form=form)

@course.route('/teacher/edit_exam/<int:id>', methods=['GET', 'POST'])
@login_required
def teacher_edit_exam(id):
    form = ExamCreateForm()
    exam = Exam.query.filter_by(id=id).first_or_404()

    if form.validate_on_submit():
        exam.name = form.name.data
        exam.date = form.date.data
        db.session.commit()

        flash('Exam Edit Successfully', 'success')

    form.name.data = exam.name
    form.date.data = exam.date

    return render_template('views/course/teacher_exam_add.html', title='Edit Exam', form=form)

@course.route('/teacher/delete_exam/<int:id>', methods=['GET', 'POST'])
@login_required
def teacher_delete_exam(id):
    exam = Exam.query.filter_by(id=id).first_or_404()
    db.session.delete(exam)
    db.session.commit()

    return redirect(url_for('course.teacher_index'))

@course.route('/student/index')
def student_index():
    courses = Course.query.filter_by(grade_level=g.student.grade_level)
    return render_template('views/course/student_index.html', title='All Courses', courses=courses)

@course.route('/student/my_courses')
def student_my_courses():
    student = Student.query.filter_by(id=g.student.id).first_or_404()
    courses = student.courses
    return render_template('views/course/student_my_courses.html', title='My Courses', courses=courses)

@course.route('/student/<int:id>')
def student_show(id):
    course = Course.query.filter_by(id=id).first_or_404()
    title = "Course: {}".format(course.name)
    exams = Exam.query.filter_by(course_id = course.id)
    return render_template('views/course/student_show.html', title=title, course=course, exams=exams)

@course.route('/student/join/<id>')
def student_join(id):
    student = Student.query.filter_by(id=g.student.id).first_or_404()
    course = Course.query.filter_by(id=id).first_or_404()
    statement = association.insert().values(student_id=student.id, course_id=course.id)
    db.session.execute(statement)
    db.session.commit()
    flash('You Joined To Course', 'success')
    return redirect(url_for('course.student_show', id=id))

@course.route('/student/left/<id>')
def student_left(id):
    student = Student.query.filter_by(id=g.student.id).first_or_404()
    course = Course.query.filter_by(id=id).first_or_404()
    student.courses.remove(course)
    db.session.commit()
    flash('You Left the Course', 'success')
    return redirect(url_for('course.student_show', id=id))

@course.route('/student/my_exams')
def student_my_exams():
    courses = Student.query.filter_by(id=g.student.id).first_or_404().courses
    return render_template('views/course/student_my_exams.html', title='My Exams', courses = courses)
