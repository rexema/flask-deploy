from flask_login import UserMixin
from sqlalchemy import Table
from blog.app import db
from flask_admin import Admin


article_tag_associations_table = Table(
    'article_tag_associations',
    db.metadata,
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), nullable=False),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'),nullable=False)
)


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    author = db.relationship("Author", uselist=False, back_populates="user")


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", back_populates="author")
    articles = db.relationship('Article', back_populates='author')


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", back_populates="articles")
    tags = db.relationship("Tag", secondary=article_tag_associations_table, back_populates='articles')

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, default="", server_default="")
    articles = db.relationship('Article',secondary=article_tag_associations_table, back_populates='tags')


