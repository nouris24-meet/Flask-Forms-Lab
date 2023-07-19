from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "nour.stety"
password = "12345"
facebook_friends=["Adam","Zena","Sam", "Sireen", "Nada", "Salma", "Kosta", "Jan"]

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		u = request.form['username'] 
		p = request.form['password'] 
		if (u==username and p==password):
			return redirect(url_for('home'))
		else:
			return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', ff=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def friend_exists(name):
    return render_template('friend_exists.html', n = name, ff=facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True)
