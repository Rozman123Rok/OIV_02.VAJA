from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# inicializiramo bazo
db = SQLAlchemy()
# dodamo ime
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'random_string' # drgace bi to mogo skrit ampak zaj ni pomembno
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # KJE IMAMO BAZO

    db.init_app(app) # inicializiramo

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    ustvari_bazo(app)

    return app

def ustvari_bazo(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Ustvaril bazo")