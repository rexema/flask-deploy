from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import AuthorSchema
from blog.app import db
from blog.models import Author, Article
from combojsonapi.event.resource import EventsResource



class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
   
    data_layer = {
        "session": db.session,
        "model": Author,
    }
