from os import getenv

from flask import Flask, render_template, g, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    @app.before_request
    def before_request():
        from app.models.student import Student

        g.student = None
        if 'student' in session:
            student = Student.query.filter_by(id = session['student']).first()
            g.student = student

    @app.context_processor
    def context_processor():
        return dict(
            site_url = "https://localhost:5000",
            site_name = "Course Finder",
            student = g.student,
        )

    from app.routes.main import main
    app.register_blueprint(main)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.profile import profile
    app.register_blueprint(profile)

    from app.routes.dashboard import dashboard
    app.register_blueprint(dashboard)

    from app.routes.course import course
    app.register_blueprint(course)

    return app
