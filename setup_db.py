from app import create_app
from app import db
from datetime import date

app = create_app()
app.app_context().push()

from app.models.teacher import Teacher
from app.models.student import Student
from app.models.course import Course
from app.models.exam import Exam

db.drop_all()
db.create_all()

teacher = Teacher()
teacher.name = 'Ömer Çulha'
teacher.email = 'omerculha@mail.com'
teacher.phone = '0000 000 00 00'
teacher.generate_password_hash('123456')
db.session.add(teacher)


student = Student()
student.name = 'Yunus Emre'
student.email = 'yunusemre@mail.com'
student.phone = '0000 000 00 00'
student.grade_level = 1
student.parent_code = "11111111111"
student.generate_password_hash('123456')
db.session.add(student)

course = Course()
course.name = 'Fen Bilgisi'
course.grade_level = 1
course.teacher = teacher
course.price = "25"
db.session.add(course)

exam = Exam()
exam.name = 'Fen Sınavı'
exam.date = date.today()
exam.course = course
db.session.add(exam)

db.session.commit()
