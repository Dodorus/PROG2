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

	list_uebergabe_rl = {}
	for d in rl:
		for key, value in d.items():
			if key == "name":
				list_uebergabe_rl_string = value + ": '{"

			elif key == "zutaten":
				for zut_name, zut_wert in d["zutaten"].items():
					zut_wert = zut_wert.replace(",", " ")
					
					list_uebergabe_rl_string = list_uebergabe_rl_string + "[" + zut_name + "," + zut_wert + "],"
				list_uebergabe_rl_string = list_uebergabe_rl_string + "}'"



	return render_template("rezepte.html", title="Rezepte", rl=rl, list_uebergabe_rl_string=list_uebergabe_rl_string)

@app.route("/rezepte/rezepte_speichern", methods=["GET", "POST"])
@login_required
def rezepte_speichern():
	form = RezeptErfassen()
	list_zutaten = {1,2,3,4,5,6,7,8,9,10}
	if form.validate_on_submit():
		R_name = form.rezeptName.data

		zutat_1 = form.zutat1.data
		zutatM_1 = form.zutatM1.data

		zutat_2 = form.zutat2.data
		zutatM_2 = form.zutatM2.data

		zutat_3 = form.zutat3.data
		zutatM_3 = form.zutatM3.data

		zutat_4 = form.zutat4.data
		zutatM_4 = form.zutatM1.data

		zutat_5 = form.zutat5.data
		zutatM_5 = form.zutatM5.data

		zutat_6 = form.zutat6.data
		zutatM_6 = form.zutatM6.data

		zutat_7 = form.zutat7.data
		zutatM_7 = form.zutatM7.data

		zutat_8 = form.zutat8.data
		zutatM_8 = form.zutatM8.data

		zutat_9 = form.zutat9.data
		zutatM_9 = form.zutatM9.data

		zutat_10 = form.zutat10.data
		zutatM_10 = form.zutatM10.data

		#dict liste machen, werte speichern
		list_zutaten = {zutat_1: zutatM_1, zutat_2: zutatM_2, zutat_3: zutatM_3, zutat_4: zutatM_4, zutat_5: zutatM_5, zutat_6: zutatM_6, zutat_7: zutatM_7, zutat_8: zutatM_8, zutat_9: zutatM_9, zutat_10: zutatM_10}

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
		    	"zutaten": list_zutaten
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


	return render_template("rezepte_speichern.html", title="Rezepte erfassen", form=form, list_zutaten=list_zutaten)