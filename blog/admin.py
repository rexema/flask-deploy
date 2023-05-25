from flask import redirect, url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from blog import models
from .app import db

# Customized admin interface


class CustomView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for("auth.login"))


class MyAdminIndexView(AdminIndexView):
    @expose("/")
    def index(self):
        if not (current_user.is_authenticated):
            return redirect(url_for("auth.login"))
        return super(MyAdminIndexView, self).index()


# Create admin with custom props
admin = Admin(
    name="Blog Admin",
    index_view=MyAdminIndexView(),
    template_mode="bootstrap4",
)

# Add views
admin.add_view(CustomView(models.User, db.session, category="Users"))
admin.add_view(CustomView(models.Author, db.session, category="Authors"))
admin.add_view(CustomView(models.Article, db.session, category="Articles"))


class TagAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True


admin.add_view(TagAdminView(models.Tag, db.session, category="Tags"))
