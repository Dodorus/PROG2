from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
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
	zutat1 = StringField('Zutat 1', validators=[DataRequired()])
	submit = SubmitField('Rezept speichern')