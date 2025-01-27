from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username2 = request.form['username']
		password2 = request.form['password']
		return render_template('response.html')

@app.route('/home')
def home():
	if request.method == 'GET':
		return render_template('home.html')  

@app.route('/friend')
def friend():
	if request.method == 'GET':
		return render_template('friend_exists.html')



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)