from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class ProfileStudentEdit(FlaskForm):
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
        render_kw={'placeholder': 'New Password'}
    )
    submit = SubmitField('Save')

class ProfileTeacherEdit(FlaskForm):
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
        render_kw={'placeholder': 'New Password'}
    )
    submit = SubmitField('Save')
