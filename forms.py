from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name_and_surname = StringField('Имя и фамилия ребёнка', validators=[DataRequired()])
    phone_number = StringField('Номер телефона законного представителя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Sign In')
