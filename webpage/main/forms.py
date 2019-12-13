from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, BooleanField, RadioField
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
	rezeptName = StringField('Name des Rezepts', validators=[DataRequired()])
	
	rezeptBild = FileField(u'Bild des Menus', validators=[FileAllowed(['jpg', 'png']), DataRequired()])

	persons = SelectField('Anzahl Personen', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])

	zutat1 = StringField('Erste Zutat', validators=[DataRequired()])
	zutatM1 = StringField('Menge (bsp: 100 oder 1)', validators=[DataRequired()])
	zutatMA1 = SelectField('Grösse (bsp: g oder kg)', choices=[('Stück', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')], validators=[DataRequired()])

	zutat2 = StringField('nächste Zutat')
	zutatM2 = StringField('Menge')
	zutatMA2 = SelectField('Grösse', choices=[('Stück', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])

	zutat3 = StringField('nächste Zutat')
	zutatM3 = StringField('Menge')
	zutatMA3 = SelectField('Grösse', choices=[('Stück', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])

	zutat4 = StringField('nächste Zutat')
	zutatM4 = StringField('Menge')
	zutatMA4 = SelectField('Grösse', choices=[('', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])

	zutat5 = StringField('nächste Zutat')
	zutatM5 = StringField('Menge')
	zutatMA5 = SelectField('Grösse', choices=[('', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])

	zutat6 = StringField('nächste Zutat')
	zutatM6 = StringField('Menge')
	zutatMA6 = SelectField('Grösse', choices=[('', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])

	zutat7 = StringField('nächste Zutat')
	zutatM7 = StringField('Menge')
	zutatMA7 = SelectField('Grösse', choices=[('', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])

	zutat8 = StringField('nächste Zutat')
	zutatM8 = StringField('Menge')
	zutatMA8 = SelectField('Grösse', choices=[('', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])

	zutat9 = StringField('nächste Zutat')
	zutatM9 = StringField('Menge')
	zutatMA9 = SelectField('Grösse', choices=[('', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])

	zutat10 = StringField('nächste Zutat')
	zutatM10 = StringField('Menge')
	zutatMA10 = SelectField('Grösse', choices=[('', 'Stück'), ('mg', 'mg'), ('kg', 'kg'), ('g', 'g'), ('tl', 'Teelöffel'), ('el', 'Esslöffel'), ('ml', 'Milliliter'), ('dl', 'Deziliter'), ('l', 'Liter')])
	
	submit = SubmitField('Rezept speichern')

class AnzPersonenForm(FlaskForm):
	personenAnz = RadioField('', coerce=int, choices=[1,2,3,4,5,6])
	submit = SubmitField('Repte')