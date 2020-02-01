# This Python file uses the following encoding: utf-8

#import aller pakete
from flask import render_template, url_for, flash, redirect, request, jsonify, make_response, session, Markup
from flask_login import login_user, current_user, logout_user, login_required
from main import app, db, bcrypt, daten
from main.forms import RegistrationForm, LoginForm, RezeptErfassen, AnzPersonenForm
from main.models import benutzer_k, aufgaben, load_user, neues_rezept_ablegen, neues_rezept_abfragen, rezept_verknuepfung_update, neuer_wochentag_ablegen
from datetime import datetime
import main.daten
import json

#import fertig
#home
@app.route("/")
def index():

	return render_template("index.html")

#übersicht
@app.route("/uebersicht")
def uebersicht():
	return render_template("uebersicht.html")

#registrieren
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

#login
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
			flash(f'Eingeloggt!', 'success')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash(f'Überprüfe E-Mail und Password.', "danger")
	return render_template("login.html", title="Login", form=form)

#logout
@app.route("/logout")
def logout():
	logout_user()
	flash(f'Ausgeloggt!', 'success')
	return redirect(url_for('index'))

#alle rezepte
@app.route("/rezepte")
@login_required
def rezepte():
	rezept_name = {}
	db = "rezepte"
	rl = neues_rezept_abfragen(rezept_name, db)

	user_session = load_user(session["user_id"])
	for t,user_id in session.items():
		if t == "user_id":
			user_id = user_id

	this = ""

	return render_template("rezepte.html", title="Rezepte", this=this, rl=rl, user_id=user_id)

#dieser prozess wird aus javascript aktiviert
@app.route('/background_process/<name>', methods=['GET', 'POST'])
def background_process(name=False):

	name = name.split(",")
	u_id = name[0]
	b_id = name[1]
	b_name = name[2]
	u_rl = rezept_verknuepfung_update(u_id,b_id,b_name)

#favoriten
@app.route("/favoriten")
@login_required
def favoriten():
	rezept_name = {}
	db = "rezepte"
	rl = neues_rezept_abfragen(rezept_name, db)

	for t,user_id in session.items():
		if t == "user_id":
			user_id = user_id

	form = AnzPersonenForm()
	if form.validate_on_submit():
		print("yes")

	return render_template("rezept_favoriten.html", title="Rezepte", form=form, rl=rl, user_id=user_id)

#wochenübersicht
@app.route("/wochensicht")
@login_required
def wochensicht():
	for t,user_id in session.items():
		if t == "user_id":
			user_id = user_id

	rezept_name = {"_id": user_id}
	db = "wochensicht"

	rezept_name_2 = {}
	rez_tag_dict = {}
	i = 1
	days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

	for weekday in days:
		rez_tag_dict[weekday] = {}
		for rp_wt in neues_rezept_abfragen(rezept_name, db):
			rp_wt = rp_wt[weekday].split(",")
			for rz_name in rp_wt:
				for vergleich_rezepte in neues_rezept_abfragen(rezept_name_2, ""):
					
					if vergleich_rezepte["name"] == rz_name:
						name = vergleich_rezepte["name"]
						rez_tag_dict[weekday][name] = {
							"img": vergleich_rezepte["img"],
							"zutaten": vergleich_rezepte["zutaten"]
						}
						
					else:
						i=0
				
	return render_template("uebersicht.html", title="Wochenübersicht", rez_tag_dict=rez_tag_dict)

#prozess wird aus javascript/jinia aktiviert
@app.route('/background_weekplan/<name>')
def background_weekplan(name=False):

	name = name.split(",")
	rez_name = name[0]
	tag = name[1]
	user_id = name[2]

	wt = neuer_wochentag_ablegen(user_id, tag, rez_name)

	return redirect(url_for('favoriten'))

#rezept speichern
@app.route("/rezepte/rezepte_speichern", methods=["GET", "POST"])
@login_required
def rezepte_speichern():
	form = RezeptErfassen()

	if form.validate_on_submit():
		R_name = form.rezeptName.data

		person_anz = form.persons.data

		if form.rezeptBild.data:
			picture_file = daten.save_pictures(form.rezeptBild.data)
			pic = picture_file

		zutat_1 = form.zutat1.data
		zutatM_1 = form.zutatM1.data
		zutatMA_1 = form.zutatMA1.data

		zutat_2 = form.zutat2.data
		zutatM_2 = form.zutatM2.data
		zutatMA_2 = form.zutatMA2.data

		zutat_3 = form.zutat3.data
		zutatM_3 = form.zutatM3.data
		zutatMA_3 = form.zutatMA3.data

		zutat_4 = form.zutat4.data
		zutatM_4 = form.zutatM4.data
		zutatMA_4 = form.zutatMA4.data

		zutat_5 = form.zutat5.data
		zutatM_5 = form.zutatM5.data
		zutatMA_5 = form.zutatMA5.data

		zutat_6 = form.zutat6.data
		zutatM_6 = form.zutatM6.data
		zutatMA_6 = form.zutatMA6.data

		zutat_7 = form.zutat7.data
		zutatM_7 = form.zutatM7.data
		zutatMA_7 = form.zutatMA7.data

		zutat_8 = form.zutat8.data
		zutatM_8 = form.zutatM8.data
		zutatMA_8 = form.zutatMA8.data

		zutat_9 = form.zutat9.data
		zutatM_9 = form.zutatM9.data
		zutatMA_9 = form.zutatMA9.data

		zutat_10 = form.zutat10.data
		zutatM_10 = form.zutatM10.data
		zutatMA_10 = form.zutatMA10.data

		#dict liste machen, werte speichern

		list_zutaten = {zutat_1: zutat_1 + "," + zutatM_1 + "," + zutatMA_1,
		zutat_2: zutat_2 + "," + zutatM_2 + "," + zutatMA_2,
		zutat_3: zutat_3 + "," + zutatM_3 + "," + zutatMA_3,
		zutat_4: zutat_4 + "," + zutatM_4 + "," + zutatMA_4,
		zutat_5: zutat_5 + "," + zutatM_5 + "," + zutatMA_5,
		zutat_6: zutat_6 + "," + zutatM_6 + "," + zutatMA_6,
		zutat_7: zutat_7 + "," + zutatM_7 + "," + zutatMA_7,
		zutat_8: zutat_8 + "," + zutatM_8 + "," + zutatMA_8,
		zutat_9: zutat_9 + "," + zutatM_9 + "," + zutatMA_9,
		zutat_10: zutat_10 + "," + zutatM_10 + "," + zutatMA_10
		}

		key = datetime.now()
		neues_rezept_ablegen(key, R_name, pic, list_zutaten, person_anz)
		

	return render_template("rezepte_speichern.html", title="Rezepte erfassen", form=form)
