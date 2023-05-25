from blog.app import create_app


app = create_app()
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,

    )


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    from blog.app import db
    db.create_all()
    print("done!")

@app.cli.command("create-tags")
def create_tags():

    from blog.models import Tag
    from blog.app import db
    for name in [
    "flask",
    "django",
    "python",
    "sqlalchemy",
    "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")

@app.cli.command("create-author")
def create_author():
    from blog.models import Author
    from blog.app import db
    author=Author(user_id='1')
    db.session.add(author)
    db.session.commit()