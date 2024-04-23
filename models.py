from sqlalchemy import String, Integer

from app import db
from app import login_manager


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    name_surname = db.Column(String(64))
    phone_number = db.Column(String(64), unique=True)
    password_hash = db.Column(String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(Integer, primary_key=True)
    name_surname = db.relationship('Users', backref='name_surname')
    comprehensive_development_2_3 = db.Column(Integer)
    comprehensive_development_3_4 = db.Column(Integer)
    comprehensive_development_4_5 = db.Column(Integer)
    musical_development = db.Column(Integer)
    art_studio_4 = db.Column(Integer)
    english_5 = db.Column(Integer)
    vocals_4_6 = db.Column(Integer)
    speech_therapist = db.Column(Integer)
    art_studio_7 = db.Column(Integer)
    english_7_11 = db.Column(Integer)
    vocals_7_11 = db.Column(Integer)
    speed_reading = db.Column(Integer)
    russian_math_intensive_courses = db.Column(Integer)
    english_grammar = db.Column(Integer)
    future_first_graders = db.Column(Integer)
    preschoolers = db.Column(Integer)

    def __repr__(self):
        return '<Course {}>'.format(self.body)


class Payments(db.Model):
    __tablename__ = 'payments'
    id = db.Column(Integer, primary_key=True)
    name_surname = db.relationship('Users', backref='name_surname')
    cost = db.Column(Integer)

    def __repr__(self):
        return '<Payment {}>'.format(self.body)
