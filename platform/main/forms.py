from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from main.models import benutzer_k

#Hier kommen Klassen für Formulare
class RegistrationForm(FlaskForm):
	username = StringField('Username', 
		validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
		validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password',
		validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = benutzer_k.query.filter_by(name_econ=username.data).first()
		if user:
			raise ValidationError('Dieser Benutzername existiert bereits.')

	def validate_email(self, email):
		user = benutzer_k.query.filter_by(email_econ=email.data).first()
		if user:
			raise ValidationError('Diese E-Mail existiert bereits.')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')

class RezeptErfassen(FlaskForm):
	rezeptName = StringField('Name', validators=[DataRequired()])
	
	rezeptBild = FileField(u'Bild des Rezepts oder des Menues', validators=[FileAllowed(['jpg', 'png'])])

	zutat1 = StringField('Erste Zutat', validators=[DataRequired()])
	zutatM1 = StringField('Menge (bsp: 100,g oder 3,kg)', validators=[DataRequired()])
	
	zutat2 = StringField('nächste Zutat')
	zutatM2 = StringField('Menge')

	zutat3 = StringField('nächste Zutat')
	zutatM3 = StringField('Menge')

	zutat4 = StringField('nächste Zutat')
	zutatM4 = StringField('Menge')

	zutat5 = StringField('nächste Zutat')
	zutatM5 = StringField('Menge')

	zutat6 = StringField('nächste Zutat')
	zutatM6 = StringField('Menge')

	zutat7 = StringField('nächste Zutat')
	zutatM7 = StringField('Menge')

	zutat8 = StringField('nächste Zutat')
	zutatM8 = StringField('Menge')

	zutat9 = StringField('nächste Zutat')
	zutatM9 = StringField('Menge')

	zutat10 = StringField('nächste Zutat')
	zutatM10 = StringField('Menge')
	
	submit = SubmitField('Rezept speichern')

class AnzPersonenForm(FlaskForm):
	personenAnz = RadioField('', coerce=int, choices=[1,2,3,4,5,6])
	submit = SubmitField('Go')