from flask_login import current_user, login_required
from werkzeug.exceptions import NotFound
from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy.orm import load_only, joinedload

from blog.forms.article import CreateArticleForm


article_app = Blueprint('article_app', __name__,
                        url_prefix='/articles', static_folder='../static')
TITLES = []


@article_app.route('/')
def article_list():
    from blog.models import Article
    articles = Article.query.all()
    return render_template('articles/list.html', articles=articles)


@article_app.route('/<int:pk>')
def get_article(pk: int):
    from blog.models import Article
    article = Article.query.filter_by(id=pk).options(joinedload(Article.tags)).one_or_none()
    if article is None:
        raise NotFound
    return render_template('articles/detail.html', article=article)


@article_app.route('/create/', methods=['GET', 'POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    from blog.models import Article, Author, Tag
    from blog.app import db
    form.tags.choices = [(tag.id, tag.name)for tag in Tag.query.order_by("name")]

    if request.method == 'POST' and form.validate_on_submit():
        article = Article(title=form.title.data, text=form.text.data)
        db.session.add(article)             
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)    

        db.session.commit()
        return redirect(url_for('article_app.get_article', pk=article.id))
    return render_template('articles/create.html', form=form)

@article_app.route('tag/<int:pk>')
def get_article_by_tag(pk: int):
    from blog.models import article_tag_associations_table, Article, Tag
    query_article = Article.query.join(article_tag_associations_table).join(Tag).filter((article_tag_associations_table.c.article_id==Article.id)&(article_tag_associations_table.c.tag_id==Tag.id)).filter(article_tag_associations_table.c.tag_id==pk)
    
    if query_article is None:
        raise NotFound
    return render_template('articles/articles_by_tag.html',articles=query_article)