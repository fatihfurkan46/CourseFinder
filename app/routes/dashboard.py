from flask import Blueprint, redirect, url_for, render_template, g
from flask_login import current_user, login_required

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('course.teacher_index'))
    elif g.student:
        return redirect(url_for('course.student_index'))
    else:
        return redirect(url_for('main.index'))
