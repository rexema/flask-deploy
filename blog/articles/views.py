from werkzeug.exceptions import NotFound
from flask import Blueprint, redirect, render_template
from sqlalchemy.orm import load_only


article_app = Blueprint('article_app', __name__, url_prefix='/articles', static_folder='../static')
TITLES = []

@article_app.route('/')

def article_list():
   
    from blog.models import Article
    articles = Article.query.all()
    
    return render_template('articles/list.html', articles=articles)

@article_app.route('/<int:pk>')
def get_article(pk:int):
    from blog.models import Article
    article = Article.query.filter_by(id=pk).one_or_none() 
    title=article.title.decode('UTF-8')   
    text=article.text.decode('UTF-8')
    return render_template('articles/detail.html', title=title, text=text)