from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from blog.user.views import user_app
from blog.articles.views import article_app
from blog.authors.views import authors
from blog.auth.views import auth
from flask import redirect, url_for
import os
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


migrate = Migrate()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    cfg_name = os.environ.get("CONFIG_NAME") or "BaseConfig"
    app.config.from_object(f'blog.config.{cfg_name}')
    register_extensions(app)
    register_blueprints(app)
    from blog.admin import admin
    admin.init_app(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from blog.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for("auth.login"))


def register_blueprints(app: Flask):
    app.register_blueprint(user_app)
    app.register_blueprint(article_app)
    app.register_blueprint(auth)
    app.register_blueprint(authors)


def register_commands(app: Flask):
    from wsgi import init_db, create_tags
    app.cli.add_command(init_db)
    app.cli.add_command(create_tags)
