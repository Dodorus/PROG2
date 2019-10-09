from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
import csv
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
nav = Nav(app)
Bootstrap(app)

app.config['SECRET_KEY'] = "c9197d0d4da6973d2ef559402929e501"

nav.register_element("my_navbar", Navbar(
	"",
	View("Welcome", "index"),
	View("Übersicht", "uebersicht"),
	View("Registrieren", "registrieren"),
	View("Login", "login")
	))

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/uebersicht")
def uebersicht():
	return render_template("uebersicht.html")

@app.route("/registrieren")
def registrieren():
	form = RegistrationForm()
	return render_template("registrieren.html", title="Registrieren", form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

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

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('_Login_')
