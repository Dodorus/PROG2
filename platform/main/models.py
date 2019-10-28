from datetime import datetime
from main import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return benutzer_k.query.get(int(user_id))

class benutzer_k(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name_econ = db.Column(db.String(20), unique=True, nullable=False)
	email_econ = db.Column(db.String(120), unique=True, nullable=False)
	firma_besch_econ = db.Column(db.String(120), nullable=True)
	image_file_econ = db.Column(db.String(20), nullable=False, default='images/default.jpg')
	password_econ = db.Column(db.String(60), nullable=False)
	auf_rel = db.relationship('aufgaben', backref='aufgabenAutor', lazy = True)

	def __repr__(self):
		return f"benutzer_k('{self.name_econ}', '{self.email_econ}', '{self.image_file_econ}'"

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