# This Python file uses the following encoding: utf-8

#import aller pakete
from datetime import datetime
from flask import flash
from main import db, login_manager, collection, wochentage
from flask_login import UserMixin
#import fertig

@login_manager.user_loader
def load_user(user_id):
	return benutzer_k.query.get(int(user_id))

#funktion um ein neues rezept abzuspeichern
def neues_rezept_ablegen(key, R_name, pic, list_zut, pers):
	rl_pruef = collection.find_one({"name": R_name})
	if rl_pruef == None:
		online_rezepts = {
			"timestamp": str(key),
		    "img" : pic,
		    "name": R_name,
		    "zutaten": list_zut,
		    "personen": pers,
		    "fav": "1"
			}

		go = collection.insert_one(online_rezepts)

		#warning wird nur ausgegeben wernn dieses ablegen des rezept auch ausgeführt wurde
	#flash('Dieser Name existiert für dieses Rezept bereits', 'warning')

		#Antwort wenn alles korrekt
		#flash('Rezept erfasst', 'success')

	else:
		print("flash nachricht raus")
		#Antwort wenn der Name bereits vorhanden ist. Name funktioniert als unique ID, eigentlich nicht so clever aber muss jetzt herhalten
		#flash('Dieser Name existiert für dieses Rezept bereits', 'warning')

def neuer_wochentag_ablegen(user_id, rez_name, tag):
	userid_pruef = wochentage.find_one({"_id": user_id})
	while userid_pruef == None:
		tag_erfassen = {
			"_id": user_id,
			"Montag": "",
			"Dienstag": "",
			"Mittwoch": "",
			"Donnerstag": "",
			"Freitag": "",
			"Samstag": "",
			"Sonntag": ""
			}
		go = wochentage.insert_one(tag_erfassen)
		break
	else:
		find_day = wochentage.find_one({"_id": user_id})
		if tag in find_day:
			for key,val in find_day.items():
				if key == tag:
					if rez_name in val:
						print("flash nachricht raus")
						#flash('Dieses Rezept ist bereits für den ' + tag + ' notiert.', 'warning')
					else:
						val = val + "," + rez_name
						go = wochentage.update_one({"_id": user_id}, {"$set": {tag:val}})
						#flash('Wurde für ' + tag + ' unter Wochenplanung eingetragen.', 'success')
		else:
			#update die favoriten
			go = wochentage.update_one({"_id": user_id}, {"$set": {tag:rez_name}})
			#flash('Wurde für ' + tag + ' eingetragen.', 'success')

#suchen der rezepte
#Rezept Abfragen. Eine Funktion für alle Abfragen, steuerbar durch die Var "db"
def neues_rezept_abfragen(rezept_name, db):
	if "wochensicht" == db:
		rezept_load = wochentage.find(rezept_name)
		return rezept_load
	else:
		rezept_load = collection.find(rezept_name)
		return rezept_load

#update rezepte pro tag in wochenübersicht, rez x hinzu oder rez x raus
#Wenn Verknüpfungen upgedatet werden wie Verbindungen zwischen den User und der Wochenplanung
def rezept_verknuepfung_update(user_id, bid, name):
	find = collection.find_one({"name":name})
	do = []
	do = find['fav']
	do = do.split(",")
	if user_id in do:
		do.remove(user_id)
	else:
		do.append(user_id)

	string_user = ",".join(do)

	collection.update_one( 
		{"name":name}, 
        { 
                "$set":{ 
                        "fav":string_user
                        }
        })



class benutzer_k(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name_econ = db.Column(db.String(20), unique=True, nullable=False)
	email_econ = db.Column(db.String(120), unique=True, nullable=False)
	firma_besch_econ = db.Column(db.String(120), nullable=True)
	image_file_econ = db.Column(db.String(20), nullable=False, default='images/default.jpg')
	password_econ = db.Column(db.String(60), nullable=False)
	auf_rel = db.relationship('aufgaben', backref='aufgabenAutor', lazy = True)

	def __repr__(self):
		return f"benutzer_k('{self.name_econ}', '{self.email_econ}', '{self.image_file_econ}')"

class aufgaben(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	titel = db.Column(db.String(20), nullable=False)
	kategorie = db.Column(db.String(100), nullable=True)
	kurzbeschriebThema = db.Column(db.String(50), nullable=True)
	anzWoerter = db.Column(db.String(20), nullable=True)
	erfassungsDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	bildJaNein = db.Column(db.String(20), nullable=True)
	word = db.Column(db.String(255), nullable=True)
	keyworte = db.Column(db.String(20), nullable=True)
	user_id = db.Column(db.Integer, db.ForeignKey('benutzer_k.id'), nullable=False)

	def __repr__(self):
		return f"aufgaben('{self.titel}', '{self.erfassungsDate}'"



