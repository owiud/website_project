from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    phone_number = StringField('Номер телефона законного представителя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти в аккаунт')


class UserForm(FlaskForm):
    name_surname = StringField('Имя и фамилия ребёнка', validators=[DataRequired()])
    phone_number = StringField('Номер телефона законного представителя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField("Авторизоваться")
