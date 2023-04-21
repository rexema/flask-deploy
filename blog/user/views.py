from werkzeug.exceptions import NotFound
from flask import Blueprint, redirect, render_template

user_app = Blueprint('user_app', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1:{'name':"Анастасия",'surname': 'Соснина'},
    2: {'name':"Мария",'surname': 'Иванова'},
    3: {'name':"Елена",'surname': 'Шарапова'},

}

@user_app.route('/')
def user_list():
    return render_template('users/list.html', users=USERS)


@user_app.route('/<int:pk>')
def get_user(pk:int):
    try:
        user = USERS[pk]
    except KeyError:
        return redirect('/users')
    return render_template('users/detail.html', user=user)