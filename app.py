from flask import Flask, render_template, flash, redirect, url_for
from flask_login import login_user, LoginManager, login_required
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from forms import LoginForm
from models import *

app = Flask(__name__)

login_manager = LoginManager()
app.config.from_object(Config)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


@app.route("/")
def main_page():
    return render_template('site.html')


@app.route("/admin")
@login_required
def admin_page():
    return render_template("admin.html")


@app.route("/rules")
def rules_page():
    return render_template('rules.html')


@app.route("/season_tickets")
def season_tickets_page():
    return "<a href='./static/files/Услуги студии 2023-2024 год .docx' download></a>"


@app.route("/offer_agreement")
def offer_agreement_page():
    return render_template('offer_agreement.html')


@app.route("/intensive_courses")
def intensive_courses_page():
    return render_template('intensives.html')


@app.route("/speed_reading")
def speed_reading_page():
    return render_template('speed_reading.html')


@app.route("/russian_math_intensive_courses")
def russian_math_intensive_courses_page():
    return render_template('russian_math_intensive_courses.html')


@app.route("/english_gramar")
def english_grammar_page():
    return render_template('english_grammar.html')


@app.route("/future_first_graders")
def future_first_graders_page():
    return render_template('future_first_graders.html')


@app.route("/comprehensive_development_2_3")
def comprehensive_development_2_3_page():
    return render_template('comprehensive_development_2_3.html')


@app.route("/comprehensive_development_3_4")
def comprehensive_development_3_4_page():
    return render_template('comprehensive_development_3_4.html')


@app.route("/comprehensive_development_4_5")
def comprehensive_development_4_5_page():
    return render_template('comprehensive_development_4_5.html')


@app.route("/musical_development")
def musical_development_page():
    return render_template('musical_development.html')


@app.route("/art_studio_4")
def art_studio_4_page():
    return render_template('art_studio_4.html')


@app.route("/english_5")
def english_5_page():
    return render_template('english_5.html')


@app.route("/vocals_4_6")
def vocals_4_6_page():
    return render_template('vocals_4_6.html')


@app.route("/speech_therapist")
def speech_therapist_page():
    return render_template('speech_therapist.html')


@app.route("/younger_students_courses")
def younger_students_courses_page():
    return render_template('junior_schoolchildren.html')


@app.route("/art_studio_7")
def art_studio_7_page():
    return render_template('art_studio_7.html')


@app.route("/english_7_11")
def english_7_11_page():
    return render_template('english_7_11.html')


@app.route("/vocals_7_11")
def vocals_7_11_page():
    return render_template('vocals_7_11.html')


@app.route("/part_time_group")
def part_time_group_page():
    return render_template('part-time.html')


@app.route("/preschool_courses")
def preschool_courses_page():
    return render_template('preschoolers.html')


@app.route("/class_zero")
def class_zero_page():
    return render_template('reviews.html')


@app.route("/schedule")
def schedule_page():
    return render_template('schedule.html')


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.name_and_surname.data).first()
        if user is None:
            hashed_pw = generate_password_hash(form.password.data, "sha256")
            user = Users(name_and_surname=form.name_and_surname.data, phone_number=form.phone_number.data,
                         password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
        name = form.name_and_surname.data
        form.name_and_surname.data = ''
        form.phone_number.data = ''
        form.password.data = ''

        flash("User Added Successfully!")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html",
                           form=form,
                           name=name,
                           our_users=our_users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.name_and_surname.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                flash("Login Succesfull!!")
                return redirect(url_for('/'))
            else:
                flash("Wrong Password - Try Again!")
        else:
            flash("That User Doesn't Exist! Try Again...")

    return render_template('login.html', form=form)


@app.errorhandler(404)
def page_not_found():
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(debug=True)
