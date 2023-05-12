from sqlite3 import IntegrityError
from flask_login import login_required, current_user, login_user
from werkzeug.exceptions import NotFound
from flask import Blueprint, redirect, render_template, request, url_for
from blog.forms.user import UserRegisterForm
from werkzeug.security import generate_password_hash


user_app = Blueprint('user_app', __name__,
                     url_prefix='/users', static_folder='../static')


@user_app.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user_app.get_user', pk=current_user.id))
    form = UserRegisterForm(request.form)
    errors = []
    from blog.models import User
    from blog.app import db
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('email not unique')
            return render_template('users/register.html', form=form)
        user = User(
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,

        )
        user.password = generate_password_hash(form.password.data)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            errors = 'Some error'
        else:
            db.session.commit()
            login_user(user)

    return render_template('users/register.html', form=form, errors=errors)


@user_app.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user_app.route('/<int:pk>')
@login_required
def get_user(pk: int):
    from blog.models import User
    user = User.query.filter_by(id=pk).one_or_none()
    return render_template('users/detail.html', user=user)
