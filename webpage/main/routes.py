from flask import render_template, url_for, flash, redirect, request, jsonify, make_response, session
from flask_login import login_user, current_user, logout_user, login_required
from main import app, db, bcrypt, daten
from main.forms import RegistrationForm, LoginForm, RezeptErfassen, AnzPersonenForm
from main.models import benutzer_k, aufgaben, load_user, neues_rezept_ablegen, neues_rezept_abfragen
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
			flash(f'Eingeloggt!', 'success')
			return redirect(next_page) if next_page else redirect(url_for('index'))
		else:
			flash(f'Überprüfe E-Mail und Password.', "danger")
	return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
	logout_user()
	flash(f'Ausgeloggt!', 'success')
	return redirect(url_for('index'))

@app.route("/rezepte")
@login_required
def rezepte():
	rezept_name = {}
	rl = neues_rezept_abfragen(rezept_name)

	user_session = load_user(session["user_id"])
	for t,user_id in session.items():
		if t == "user_id":
			user_id = user_id

	form = AnzPersonenForm()
	if form.validate_on_submit():
		print("yes")

	return render_template("rezepte.html", title="Rezepte", rl=rl, user_id=user_id, form=form)

@app.route('/background_process/<name>', methods=['GET', 'POST'])
def background_process(name=False):

	"""
	name = name.split(",")
	id_1 = name[0]
	name_1 = name[1]
	date = datetime.now()
	klicked = "klicked"
	gefunden = False
	gefunden_2 = False

	#test wenn rezepte.html verändert wird, richtige Werteübergabe von Ajax
	#print(id_1,name_1)
	
	datei_ver = 'rezepte_verwaltung.json'
	datei_inhalt_ver = daten.load_json(datei_ver)

	for a in datei_inhalt_ver['rezepte_verwaltung']:
		if gefunden == False:
			for b,c in a.items():
				if b == name_1:
				#b ist id des rezepts, c ist inhalt des rezepts
					for f in c:
						for userid_of_rezept, inhaltrezept in f.items():
							if userid_of_rezept == id_1:
								if gefunden == False:
									print(inhaltrezept["status"])
									if inhaltrezept["status"] == "btn-success":
										inhaltrezept["status"] = ""
										gefunden = True
										break
									elif inhaltrezept["status"] == "":
										inhaltrezept["status"] = "btn-success"
										gefunden = True
										break
									else:
										print("else1")
										break
								else:
									break


							else:
								print("falsche ID")
								

				else:
					#if b hier fertig
					break

		elif gefunden == False:
			datei_inhalt_ver['rezepte_verwaltung'].append({
				name_1: [{
				id_1:{
				"timestamp": str(date),
				"status": klicked
				}}]
			})
			gefunden = True
			break
			#if id==id hier fertig
		else:
			print("")

	daten.save_json(datei_ver, datei_inhalt_ver)

"""

@app.route("/favoriten")
@login_required
def favoriten():
	rezeptload = daten.load_values()
	rl = rezeptload["rezepte"]

	datei_ver = 'rezepte_verwaltung.json'
	rezept_ver_load = daten.load_json(datei_ver)
	rl_v = rezept_ver_load["rezepte_verwaltung"]
	testing = "False"

	for t,user_id in session.items():
		if t == "user_id":
			user_id = user_id

	return render_template("rezept_favoriten.html", title="Rezepte", rl=rl, user_id=user_id, rl_v=rl_v)


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
