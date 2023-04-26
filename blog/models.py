from flask_login import UserMixin
from blog.app import db



class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    articles = db.relationship('Article', backref='author')

class Article(db.Model):
     
     id = db.Column(db.Integer, primary_key = True)    
     title = db.Column(db.String(200))
     text = db.Column(db.String)
     author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
