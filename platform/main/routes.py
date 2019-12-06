from flask import render_template, url_for, flash, redirect, request, jsonify, make_response, session
from flask_login import login_user, current_user, logout_user, login_required
from main import app, db, bcrypt, daten
from main.forms import RegistrationForm, LoginForm, RezeptErfassen, AnzPersonenForm
from main.models import benutzer_k, aufgaben, load_user
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
	user_session = load_user(session["user_id"])
	for t,user_id in session.items():
		if t == "user_id":
			user_id = user_id

	datei_ver = 'rezepte_verwaltung.json'
	rezept_ver_load = daten.load_json(datei_ver)
	rl_v = rezept_ver_load["rezepte_verwaltung"]
	testing = 'False'
	
	form = AnzPersonenForm()
	if form.validate_on_submit():
		print("yes")

	return render_template("rezepte.html", title="Rezepte", form=form, rl=rl, user_id=user_id, rl_v=rl_v)

@app.route('/background_process/<name>', methods=['GET', 'POST'])
def background_process(name=False):
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
	list_zutaten = {1,2,3,4,5,6,7,8,9,10}
	if form.validate_on_submit():
		R_name = form.rezeptName.data

		if form.rezeptBild.data:
			picture_file = daten.save_pictures(form.rezeptBild.data)
			pic = picture_file

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
		    	"img" : pic,
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
