from wtforms import StringField, validators, PasswordField, SubmitField
from flask_wtf import FlaskForm


class UserRegisterForm(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last name")
    email = StringField(
        "E-mail", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", [validators.DataRequired(), validators.EqualTo(
        'confirm_password', message="Пароль не совпадает")])
    confirm_password = PasswordField(
        "Confirm password", [validators.DataRequired()])
    submit = SubmitField("Register")
