from flask import (Flask, g, render_template, flash, redirect, url_for, request)
from flask_login import (LoginManager, login_user, logout_user, login_required)
from flask_bcrypt import generate_password_hash, check_password_hash

import models

DEBUG = True
PORT = 8000
HOST = '127.0.0.1'

app = Flask(__name__)
app.secret_key = 'secret_key!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
def multiply(num1, num2):
	context = {'num1': num1, 'num2': num2}
	return render_template('multiply.html', **context)

@app.route('/user/<string:username>')
def show(username):
	return render_template('username.html', username=username)

@app.route('/contact')
def contact():
	signed_in = True
	return render_template('contact.html', signed_in=signed_in)

if __name__ == '__main__':
	# models.initialize()
	app.run(debug=DEBUG, host=HOST, port=PORT)