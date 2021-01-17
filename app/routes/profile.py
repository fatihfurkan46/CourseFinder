from flask import Blueprint, render_template, g, flash
from flask_login import current_user

profile = Blueprint('profile', __name__, url_prefix='/profile')

from app import db
from app.models.student import Student
from app.models.teacher import Teacher
from app.forms.profile import ProfileStudentEdit, ProfileTeacherEdit

@profile.route('/student', methods=['GET', 'POST'])
def student_edit():
    form = ProfileStudentEdit()
    student = Student.query .filter_by(id=g.student.id).first_or_404()

    if form.validate_on_submit():
        student.name = form.name.data
        student.phone = form.phone.data
        student.grade_level = form.grade_level.data
        student.parent_code = form.parent_code.data
        student.email = form.email.data

        if form.password.data:
            student.generate_password_hash(form.password.data)

        db.session.commit()
        flash('Profile Update Successfully', 'success')

    form.name.data = student.name
    form.phone.data = student.phone
    form.grade_level.data = student.grade_level
    form.parent_code.data = student.parent_code
    form.email.data = student.email

    return render_template('views/profile/student_edit.html', title='Profile Edit', form=form)

@profile.route('/teacher', methods=['GET', 'POST'])
def teacher_edit():
    form = ProfileTeacherEdit()
    teacher = Teacher.query .filter_by(id=current_user.id).first_or_404()

    if form.validate_on_submit():
        teacher.name = form.name.data
        teacher.phone = form.phone.data
        teacher.email = form.email.data

        if form.password.data:
            teacher.generate_password_hash(form.password.data)

        db.session.commit()
        flash('Profile Update Successfully', 'success')

    form.name.data = teacher.name
    form.phone.data = teacher.phone
    form.email.data = teacher.email

    return render_template('views/profile/teacher_edit.html', title='Profile Edit', form=form)
