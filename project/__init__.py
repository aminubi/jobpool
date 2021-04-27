from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
	return "Hello "


from project.Admin import admin as ad
app.register_blueprint(ad, url_prefix='/admin')

from project.Candidate import candidate as ca
app.register_blueprint(ca, url_prefix='/admin')

from project.Employer import employer as em
app.register_blueprint(em, url_prefix='/admin')