from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app.models.teacher import Teacher

class TeacherLoginForm(FlaskForm):
    email = StringField(
        'E-Mail',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'E-Mail', 'autofocus': True},
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Password'}
    )
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class TeacherRegisterForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Name', 'autofocus': True}
    )
    email = StringField(
        'E-Mail',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'E-Mail'}
    )
    phone = StringField(
        'Phone',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Phone'}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Password'}
    )
    password_confirm = PasswordField(
        'Password Confirm',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'placeholder': 'Password Confirm'}
    )
    submit = SubmitField('Register')

class StudentRegisterForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Name', 'autofocus': True}
    )
    email = StringField(
        'E-Mail',
        validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'E-Mail'}
    )
    phone = StringField(
        'Phone',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Phone'}
    )
    grade_level = IntegerField(
        'Grade Level',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Grade Level'}
    )
    parent_code = StringField(
        'Parent Code (TC)',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Parent Code (TC)'}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Password'}
    )
    password_confirm = PasswordField(
        'Password Confirm',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'placeholder': 'Password Confirm'}
    )
    submit = SubmitField('Register')
