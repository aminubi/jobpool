from flask import Flask,redirect,url_for,render_template,request
from project.settings import DB_SQLITE,DB_MYSQL, KEY
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY'] = KEY
#app.config['SQLALCHEMY_DATABASE_URI'] = DB_MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = DB_SQLITE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#Database Initiation
db.init_app(app)
# with app.app_context():
#    db.create_all()

@app.route('/')
def home():
	return "Hello "

from project.Admin import admin as ad
app.register_blueprint(ad, url_prefix='/admin')

from project.Candidate import candidate as ca
app.register_blueprint(ca, url_prefix='/admin')

from project.Employer import employer as em
app.register_blueprint(em, url_prefix='/admin')

from project.Auth import auth as at
app.register_blueprint(at)

from project.Account import account as acc
app.register_blueprint(acc)