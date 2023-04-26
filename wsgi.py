from blog.app import create_app, db
from werkzeug.security import generate_password_hash


app = create_app()
if __name__== '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
       
    )

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("done!")

@app.cli.command('create-user')
def create_user():
    from blog.models import User
    admin = User(email="admin@mail.ru", password =generate_password_hash('test123'))
    james = User(email="james@mailru", password=generate_password_hash('test342'))
    db.session.add(admin)
    db.session.add(james)
    db.session.commit()

@app.cli.command('create-article')
def create_article():
    from blog.models import Article
    article_1 = Article(title='Картина в картине и еще раз в картине — художественная рекурсия!'.encode('UTF-8'), text='Кто из нас не стоял между двумя зеркалами, вглядываясь в бесконечно повторяющееся изображение самого себя, вглядывающегося в в бесконечно повторяющееся изображение самого себя?.. По-научному это явление называется рекурсией, и оно нашло отражение во многих областях, начиная от физики и программирования, заканчивая искусством.'.encode('UTF-8'), author_id=1)
    article_2 = Article(title='Отпечатки ладоней возрастом 13 000 лет'.encode('UTF-8'), text= 'Можно ли прикоснуться к древности? Не к произведениям античных скульпторов и строителей, а к эпохам, оставшимся давно в прошлом? Живя в современном мире, мы редко задумываемся, насколько давно населяет Землю человек. Все началось еще миллионы лет назад, когда первые гоминиды встали на задние конечности и научились создавать примитивные орудия труда. Современная эпоха с письменностью, городами и государствами — всего лишь миг по сравнению с теми временами, когда по континентам мигрировали немногочисленные племена наших предков.'.encode('UTF-8'), author_id=2)
    db.session.add(article_1)
    db.session.add(article_2)
    db.session.commit()