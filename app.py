from flask import Flask, render_template, flash, redirect, request, url_for, g
from flask_login import login_user, LoginManager, UserMixin, logout_user, current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from forms import UserForm

app = Flask(__name__)

login_manager = LoginManager()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = "1234"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
db = SQLAlchemy(app)
migrate = Migrate()
login_manager.init_app(app)
migrate.init_app(app, db)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).get(user_id)


@app.before_request
def before_request():
    g.user = current_user
    g.username = g.user.get_id()


class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name_surname = db.Column(db.String(256), nullable=False)
    phone_number = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<User {self.name_surname}"

    def __init__(self, name_surname, phone_number, password):
        self.name_surname = name_surname
        self.phone_number = phone_number
        self.password = password

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    @classmethod
    def get_user_by_name_surname(cls, name_surname):
        return cls.query.filter_by(name_surname=name_surname).first()

    def save(self):
        db.session.add(self)
        db.session.commit()


class Courses(db.Model, UserMixin):
    __tablename__ = 'courses'
    id = db.Column(db.Integer(), primary_key=True)
    comprehensive_development_2_3 = db.Column(db.Integer(), nullable=False)
    comprehensive_development_3_4 = db.Column(db.Integer(), nullable=False)
    comprehensive_development_4_5 = db.Column(db.Integer(), nullable=False)
    musical_development = db.Column(db.Integer(), nullable=False)
    art_studio_4 = db.Column(db.Integer(), nullable=False)
    english_5 = db.Column(db.Integer(), nullable=False)
    vocals_4_6 = db.Column(db.Integer(), nullable=False)
    speech_therapist = db.Column(db.Integer(), nullable=False)
    art_studio_7 = db.Column(db.Integer(), nullable=False)
    english_7_11 = db.Column(db.Integer(), nullable=False)
    vocals_7_11 = db.Column(db.Integer(), nullable=False)
    speed_reading = db.Column(db.Integer(), nullable=False)
    russian_math_intensive_courses = db.Column(db.Integer(), nullable=False)
    english_grammar = db.Column(db.Integer(), nullable=False)
    future_first_graders = db.Column(db.Integer(), nullable=False)
    preschoolers = db.Column(db.Integer(), nullable=False)

    name_surname = db.Column(db.String(256), db.ForeignKey("users.name_surname"))

    def __repr__(self):
        return f"<Name {self.name_surname}"


class Payments(db.Model, UserMixin):
    __tablename__ = 'payments'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    cost = db.Column(db.Integer(), nullable=False)

    name_surname = db.Column(db.String(256), db.ForeignKey("users.name_surname"))

    def __repr__(self):
        return '<Payment {}>'.format(self.body)


class Teachers(db.Model, UserMixin):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer(), primary_key=True)

    name_surname = db.Column(db.String(256), db.ForeignKey("users.name_surname"))

    def __repr__(self):
        return f"<Teacher {self.name_surname}"


@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)


@app.route("/")
def main_page():
    print(f"MAIN_PAGE: {current_user.is_authenticated}")
    return render_template('site.html')


@app.route("/admin")
def admin_page():
    return render_template("admin.html")


@app.route("/rules")
def rules_page():
    return render_template('rules.html')


@app.route("/season_tickets")
def season_tickets_page():
    return "<a href='./static/files/Услуги студии 2023-2024 год .docx' download></a>"


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


@app.route("/art_studio_7")
def art_studio_7_page():
    return render_template('art_studio_7.html')


@app.route("/english_7_11")
def english_7_11_page():
    return render_template('english_7_11.html')


@app.route("/vocals_7_11")
def vocals_7_11_page():
    return render_template('vocals_7_11.html')


@app.route("/preschool_courses")
def preschool_courses_page():
    return render_template('preschoolers.html')


@app.route('/authorization', methods=['GET', 'POST'])
def authorization_page():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(name_surname=request.form.get("name_surname"),
                                     phone_number=request.form.get("phone_number")).first()

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                flash("Вход в аккаунт выполнен успешно.")
                return redirect("/personal_account")
            else:
                flash("Неправильный пароль.")
                return redirect("/authorization")

        else:
            hashed_pw = generate_password_hash(form.password.data)
            user = Users(name_surname=request.form.get("name_surname"), phone_number=request.form.get("phone_number"),
                         password=hashed_pw)
            db.session.add(user)
            db.session.commit()
            print(f"AUTHORIZATION_PAGE: {current_user.is_authenticated}")
            return redirect(url_for("personal_account_page"))

    return render_template("authorization.html", form=form)


@app.route('/personal_account')
def personal_account_page():
    print(f"PERSONAL_ACCOUNT_PAGE: {current_user.is_authenticated}")
    return render_template("personal_account.html")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You Have Been Logged Out!  Thanks For Stopping By...")
    return redirect('/authorization')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
