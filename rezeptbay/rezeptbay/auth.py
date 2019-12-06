from flask import Blueprint, render_template, url_for, flash, request, session, redirect
from .extentions import mongo
from .extentions import login_manager
import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		users = mongo.db.users
		login_user = users.find_one({'name' : request.form['username']})

		password = request.form['pass'].encode('utf-8')
		hashed = bcrypt.hashpw(password, bcrypt.gensalt())
		pw = login_user['password']
		user_id = login_user['username']
		# Check if password matches the hashed password

		if bcrypt.checkpw(password, pw):
			#flash("Eingeloggt")
			login_user(login)
		    return redirect(url_for('main.rezepte'))
		else:
		    return redirect(url_for('main.index'))

	return render_template("login.html")

@auth.route('/register', methods=['POST', 'GET'])
def register():
	#if current_user.is_authenticated:
		#return redirect(url_for('main.index'))
	if request.method == 'POST':
		users = mongo.db.users
		existing_user = users.find_one({'name': request.form['username']})

		if existing_user is None:
			passwort = request.form['pass'].encode('utf-8')
			hashpass = bcrypt.hashpw(passwort, bcrypt.gensalt())
			users.insert({'name': request.form['username'], 'password' : hashpass})
			return redirect(url_for('main.index'))

		return 'That username already exists'
		
	return render_template("registrieren.html")

@auth.route('/logout')
def logout():
		return redirect(url_for('main.index'))