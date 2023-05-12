from wtforms import StringField, validators, PasswordField, SubmitField
from flask_wtf import FlaskForm


class UserAuthForm(FlaskForm):
    email = StringField(
        "E-mail", [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", [validators.DataRequired()])
    submit = SubmitField("Log in")
