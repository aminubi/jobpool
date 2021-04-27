from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    phone = db.Column(db.String(100))
	account_number = db.Column(db.String(100))
	account_name = db.Column(db.String(100))
	bank_name = db.Column(db.String(100))
	account_status =db.Column(db.String(100))
	register_date = db.Column(db.DateTime)

class Employers(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
	company_name= db.Column(db.String(100))
    password = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    phone = db.Column(db.String(100))
	account_status =db.Column(db.String(100))
	register_date = db.Column(db.DateTime)
	job_id =  db.relationship('Jobs', backref='user', uselist=False)

class Jobs(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	job_title= db.Column(db.String(100))
	job_description = db.Column(db.String(100))
	job_type = db.Column(db.String(100))
	job_duration = db.Column(db.String(100))
	job_date = db.Column(db.String(100))
	job_status = db.Column(db.String(100))
	emp_id = db.Column(db.Integer, db.ForeignKey('employers.id'))