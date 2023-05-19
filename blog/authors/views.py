from flask import Blueprint, redirect, render_template, request, url_for


authors = Blueprint('authors', __name__,
                     url_prefix='/authors', static_folder='../static')

@authors.route('/')
def authors_list():
    from blog.models import Author
    authors = Author.query.all()
    return render_template('authors/list.html', authors=authors)
