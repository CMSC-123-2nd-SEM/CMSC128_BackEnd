from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path
from flask_login import LoginManager
from flask_executor import Executor

db = SQLAlchemy()
DB_NAME = "testing.db"

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config['SECRET_KEY'] = '8DMC9QP_ppb_7-spe_tppDB07zSaABvDIRHjbvUvgtkAj_JQqSy3UsC2l00o4VWMGsiJPujsxYn06ZJS9HnQuQ'
app.config["FILE_UPLOADS"] = "C:/Users/Sean/Desktop/CMSC128Project/Testing"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["PDF"]
app.config["MAX_FILE_FILESIZE"] = 32 * 1000 * 1000
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['REQUESTS_PER_PAGE'] = 5

db.init_app(app)

executor = Executor(app)

login = LoginManager()
login.login_view = 'auth.login'
login.init_app(app)


from .views import views
from .admin_views import admin_views
from .auth import auth

app.register_blueprint(views, url_prefix = '/')
app.register_blueprint(admin_views, url_prefix = '/')
app.register_blueprint(auth, url_prefix = '/')


from .models import Request

with app.app_context():
	db.create_all()






















