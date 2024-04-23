from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField


# Create Login Form
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    favorite_color = StringField("Favorite Color")
    about_author = TextAreaField("About Author")
    password_hash = PasswordField('Password', validators=[DataRequired(),
                                                          EqualTo('password_hash2', message='Passwords Must Match!')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    profile_pic = FileField("Profile Pic")
    submit = SubmitField("Submit")


class PasswordForm(FlaskForm):
    email = StringField("What's Your Email", validators=[DataRequired()])
    password_hash = PasswordField("What's Your Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

