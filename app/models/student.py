from werkzeug.security import generate_password_hash, check_password_hash

from app import db

association = db.Table('association',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(94), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    grade_level = db.Column(db.Integer, nullable=False)
    parent_code = db.Column(db.String(11), nullable=False)
    courses = db.relationship("Course", secondary=association, backref="students")

    def generate_password_hash(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
