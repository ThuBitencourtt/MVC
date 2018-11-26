from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user
from app import app, db, lm

from app.models.tables import User
from app.models.tables import Livro
from app.models.forms import LoginForm
from app.models.forms import CadastroForm
from app.models.forms import Cadastro_livroForm

@lm.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
	livro = Livro.query.all()
	return render_template("lista.html", livro=livro)
	
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

@app.route("/lista")
def lista():
	livro = Livro.query.all()
	return render_template("lista.html", livro=livro)

@app.route("/excluir/<int:id>")
def excluir(id):
	livro = Livro.query.filter_by(id=id).first()

	db.session.delete(livro)
	db.session.commit()

	livro = Livro.query.all()
	return render_template("lista.html", livro=livro)


@app.route("/cadastro_livro", methods=["GET", "POST"])
def cadastrar_livros():
	form = Cadastro_livroForm()				
	if request.method == "POST":
		livro = request.form.get("livro")
		autor = request.form.get("autor")
		editora = request.form.get("editora")
		cidade = request.form.get("cidade")

		if livro and autor and editora and cidade:
			post = Livro(livro,autor,editora,cidade)
			db.session.add(post)
			db.session.commit()

		return redirect(url_for("lista"))
		
	return render_template('cadastrar_livros.html',
							form=form)

