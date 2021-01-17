from flask import Blueprint, redirect, url_for, render_template, request, flash, session
from flask_login import login_user, logout_user, current_user

from app import db
from app.models.teacher import Teacher
from app.models.student import Student
from app.forms.auth import TeacherLoginForm, TeacherRegisterForm, StudentRegisterForm

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/teacher/login', methods=['GET', 'POST'])
def teacher_login():
    if current_user.is_authenticated:
        return redirect(url_for('course.teacher_index'))

    form = TeacherLoginForm()

    if form.validate_on_submit():
        teacher = Teacher.query.filter_by(email=form.email.data).first()
        if teacher is None or not teacher.check_password(form.password.data):
            flash('Login Failed', 'danger')
        else:
            login_user(teacher, remember=form.remember_me.data)
            return redirect(url_for('course.teacher_index'))

    return render_template('views/auth/teacher_login.html', title='Teacher Login', form=form)

@auth.route('/teacher/register', methods=['GET', 'POST'])
def teacher_register():
    if current_user.is_authenticated:
        return redirect(url_for('course.teacher_index'))

    form = TeacherRegisterForm()

    if form.validate_on_submit():
        teacher = Teacher(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data
        )

        teacher.generate_password_hash(form.password.data)

        db.session.add(teacher)
        db.session.commit()

        flash('Successful! You Can Login', 'success')

    return render_template('views/auth/teacher_register.html', title='Teacher Register', form=form)

@auth.route('/teacher/logout')
def teacher_logout():
    logout_user()
    flash('Logout Successful', 'success')
    return redirect(url_for('auth.teacher_login'))

@auth.route('/student/login', methods=['GET', 'POST'])
def student_login():
    form = TeacherLoginForm()

    if form.validate_on_submit():
        student = Student.query.filter_by(email=form.email.data).first()
        if student is None or not student.check_password(form.password.data):
            flash('Login Failed', 'danger')
        else:
            session['student'] = student.id
            return redirect(url_for('course.student_index'))
    return render_template('views/auth/student_login.html', title='Student Register', form=form)

@auth.route('/student/register', methods=['GET', 'POST'])
def student_register():
    form = StudentRegisterForm()

    if form.validate_on_submit():
        student = Student(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            grade_level=form.grade_level.data,
            parent_code=form.parent_code.data
        )

        student.generate_password_hash(form.password.data)

        db.session.add(student)
        db.session.commit()

        flash('Successful! You Can Login', 'success')

    return render_template('views/auth/student_register.html', title='Student Register', form=form)

@auth.route('/student/logout')
def student_logout():
    session.pop('student', None)
    return redirect(url_for('auth.student_login'))
