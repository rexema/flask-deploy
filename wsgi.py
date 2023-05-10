from blog.app import create_app, db, migrate
from werkzeug.security import generate_password_hash

app = create_app()


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,

    )


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("done!")
