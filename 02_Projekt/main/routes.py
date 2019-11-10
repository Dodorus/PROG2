from flask import render_template, url_for, flash, redirect, request, jsonify, make_response
from flask_login import login_user, current_user, logout_user, login_required
from main import app, db, bcrypt, daten
from main.forms import RegistrationForm, LoginForm, RezeptErfassen
from main.models import benutzer_k, aufgaben
from datetime import datetime
import main.daten
import json

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/uebersicht")
def uebersicht():
	return render_template("uebersicht.html")

@app.route("/registrieren", methods=['GET', "POST"])
def registrieren():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
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
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = benutzer_k.query.filter_by(email_econ=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password_econ, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash('Überprüfe E-Mail und Password.', "danger")
	return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route("/rezepte")
@login_required
def rezepte():
	rezeptload = daten.load_values()
	rl = rezeptload["rezepte"]

	return render_template("rezepte.html", title="Rezepte", rl=rl)

@app.route("/rezepte/rezepte_speichern", methods=["GET", "POST"])
@login_required
def rezepte_speichern():
	form = RezeptErfassen()
	if form.validate_on_submit():
		R_name = form.rezeptName.data
		zutat_1 = form.zutat1.data

		def speichern(datei, key, Rname, zutat1):
		    try:
		        with open(datei) as open_file:
		            datei_inhalt = json.load(open_file)
		    except FileNotFoundError:
		        datei_inhalt = {}

		    # Daten werden eingelesen
		    #datei_inhalt['rezepte'] = []
		    datei_inhalt['rezepte'].append({
		    	"id": str(key),
		    	"name": Rname,
		    	"zutaten": {
		    		"1": zutat1,
		    	}
		    })
		    print(datei_inhalt)

		    with open(datei, "w") as open_file:
		        json.dump(datei_inhalt, open_file)

		def aktivitaet_speichern(R_name, zutat_1):
		    datei_name = "rezepte_data.json"
		    zeitpunkt = datetime.now()
		    speichern(datei_name, zeitpunkt, R_name, zutat_1)
		    return zeitpunkt, R_name, zutat_1


		aktivitaet_speichern(R_name, zutat_1)


	return render_template("rezepte_speichern.html", title="Rezepte erfassen", form=form)