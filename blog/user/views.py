from flask_login import login_required
from werkzeug.exceptions import NotFound
from flask import Blueprint, redirect, render_template



user_app = Blueprint('user_app', __name__, url_prefix='/users', static_folder='../static')


@user_app.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user_app.route('/<int:pk>')
@login_required
def get_user(pk:int):
    from blog.models import User
    user = User.query.filter_by(id=pk).one_or_none()       
    return render_template('users/detail.html', user=user)


