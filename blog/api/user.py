from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import UserSchema
from blog.app import db
from ..models import User
from blog.permission.user import UserPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
       
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserPermission],}
