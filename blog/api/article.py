from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import ArticleSchema
from blog.app import db
from blog.models import Article
from combojsonapi.event.resource import EventsResource


class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count": Article.query.count()}

   

class ArticleDetailEvents(EventsResource):
    def event_get_count_by_author(self,  **kwargs):
        return {'count': Article.query.filter(Article.author_id== kwargs["id"]).count()}


class ArticleList(ResourceList):
    schema = ArticleSchema
    events = ArticleListEvents
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    events = ArticleDetailEvents
    data_layer = {
        "session": db.session,
        "model": Article,
    }

class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count": Article.query.count()}