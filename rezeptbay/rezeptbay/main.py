from flask import Blueprint, render_template, url_for, request, session, redirect
from .extentions import mongo
from .extentions import login_manager
from flask_login import login_user, current_user, login_required
import bcrypt

main = Blueprint('main', __name__)


@main.route('/')
def index():

	return render_template("index.html")

@main.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		users = mongo.db.users
		login_ser = users.find_one({'name' : request.form['username']})

		password = request.form['pass'].encode('utf-8')
		hashed = bcrypt.hashpw(password, bcrypt.gensalt())
		pw = login_ser['password']
		# Check if password matches the hashed password

		if bcrypt.checkpw(password, pw):
		    user_obj = User(login_ser['_id'])
            login_user(user_obj)
		    flash('You were successfully logged in')
		    return redirect(url_for('main.index'))
		else:
		    flash("Invalid credentials", "warning")

	return render_template("login.html")

@main.route('/register', methods=['POST', 'GET'])
def register():
	if request.method == 'POST':
		users = mongo.db.users
		existing_user = users.find_one({'name': request.form['username']})

		if existing_user is None:
			passwort = request.form['pass'].encode('utf-8')
			hashpass = bcrypt.hashpw(passwort, bcrypt.gensalt())
			users.insert({'name': request.form['username'], 'password' : hashpass})
			session['username'] = request.form['username']
			return redirect(url_for('main.index'))

		return 'That username already exists'
		
	return render_template("registrieren.html")

@main.route('/logout')
def logout():
		session.clear()
		return redirect(url_for('main.index'))

@main.route('/rezepte')
def rezepte():
		
	return render_template("account.html")

@main.route('/favoriten')
def favoriten():
		
	return render_template("account.html")
