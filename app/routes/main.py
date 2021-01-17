from flask import Blueprint, render_template, request

from app.models.student import Student

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
    return render_template('views/main/index.html')

@main.route('/info', methods=['GET', 'POST'])
def info():
    parent_code = request.args.get('parent_code')
    email = request.args.get('email')

    if not parent_code or not email:
        return render_template('views/main/error.html')

    student = Student.query.filter_by(parent_code=parent_code).filter_by(email=email).first()

    if not student:
        return render_template('views/main/error.html')


    return render_template('views/main/info.html', title='Parent Info', student=student)
