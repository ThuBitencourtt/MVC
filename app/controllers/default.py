from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User
from app.models.forms import LoginForm
from app.models.forms import CadastroForm

@lm.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():									
		user = User.query.filter_by(username=form.username.data).first()
		if user and user.password == form.password.data:
			login_user(user)
			flash("Logged in.")
			return redirect(url_for("index"))
		else:
			flash("Invalid login.")
	else:
		print(form.errors)
	return render_template('login.html',
							form=form)

@app.route("/logout")
def logout():
	logout_user()
	flash("Logged out. ")
	return redirect(url_for("index"))

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
	form = CadastroForm()				
	if request.method == "POST":
		username = request.form.get("username")
		password = request.form.get("password")
		name = request.form.get("name")
		email = request.form.get("email")

		if username and password and name and email:
			p = User(username,password,name,email)
			db.session.add(p)
			db.session.commit()

		return redirect(url_for("login"))
		
	return render_template('cadastro.html',
							form=form)

