from os import path

class Config():
    basedir = path.abspath(path.dirname(__file__))

    SECRET_KEY = "dXp1bG1lIGJhemVuIG9sbWVrIGJpbGUgaW5zYW4gaWNpbiB1bXV0dHVy"
    PORT = 80
    DEBUG = False
    TESTING = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'coursefinder.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
