
from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.models import Tag
from blog.schemas import TagSchema


class TagList(ResourceList):
    from blog.app import db
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag
    }


class TagDetail(ResourceDetail):
    from blog.app import db
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag
    }
