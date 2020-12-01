#!/usr/bin/ env python
from flask import Flask,request,render_template
from flaskext.mysql import mySQL

mysql=mySQL()
app=flask.Flask(__name__)
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='test'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)



@app.route('/')

def login_form():
	return render_template('login_page.html')

@app.route('/',methods=['POST'])

def Authenticate():
	username=request.form['username']
	password=request.form['password']
	cursor=mysql.connect().cursor()
	cursor.execute("SELECT* from user where username='"+ username +"' and password='"+ password +"'")
	data=cursor.fetchone()

	if data is None:
		return "Either username or password is wrong"
	else:
		return "Login Succesful"


app.config["DEBUG"]=True
app.run()