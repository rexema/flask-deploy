from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required
from werkzeug.security import check_password_hash

from blog.forms.auth import UserAuthForm

auth = Blueprint("auth", __name__, static_folder="../static")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = UserAuthForm(request.form)
    from blog.models import User
    if request.method == "GET":

        return render_template("auth/login.html", form=form)
    email = request.form.get("email")
    password = request.form.get("password")
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=email).first()
        if not user and check_password_hash(user.password, password):
            return render_template("auth/login.html", form=form)

        login_user(user)
        return redirect(url_for("user_app.get_user", pk=user.id))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
