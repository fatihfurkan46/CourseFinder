from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired

class CourseCreateForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Name', 'autofocus': True},
    )
    grade_level = IntegerField(
        'Grade Level',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Grade Level'}
    )
    price = StringField(
        'Price',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Price', 'autofocus': True},
    )
    submit = SubmitField('Create Course')

class CourseEditForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Name', 'autofocus': True},
    )
    grade_level = IntegerField(
        'Grade Level',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Grade Level'}
    )
    price = StringField(
        'Price',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Price', 'autofocus': True},
    )
    submit = SubmitField('Save Course')

class ExamCreateForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Name', 'autofocus': True},
    )
    date = DateField(
        'Date',
        validators=[DataRequired()],
        render_kw={'placeholder': 'Date - Ex: 2021-01-30', 'type': 'date'}
    )
    submit = SubmitField('Save Exam')
