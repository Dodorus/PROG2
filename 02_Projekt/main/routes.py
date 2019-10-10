from flask import render_template, url_for, flash, redirect
from main import app, db, bcrypt
from main.forms import RegistrationForm, LoginForm
from main.models import benutzer_k, aufgaben


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/uebersicht")
def uebersicht():
	return render_template("uebersicht.html")

@app.route("/registrieren", methods=['GET', "POST"])
def registrieren():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = benutzer_k(name_econ=form.username.data, email_econ=form.email.data, password_econ=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('login'))
	return render_template("registrieren.html", title="Registrieren", form=form)

@app.route("/login", methods=['GET', "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'dominic-kunz@hotmail.com' and form.password.data == "password":
			flash("You have been logged in!", "success")
			return redirect(url_for('index'))
		else:
			flash('Login Unsuccessful. Pleas try again.', "danger")
	return render_template("login.html", title="Login", form=form)
