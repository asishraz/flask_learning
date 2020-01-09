from flask import Flask, render_template

app = Flask(__name__)


# #understanding the use of url_for() in flask and rendering the html file in flask_python file 
# @app.route('/profile/<name>')
# def profile(name):
# 	return render_template('profile.html', name=name)


#how to use multiple urls in a single flask file
@app.route('/')
@app.route("/<user>")
def index(user=None):
	return render_template("user.html", user=user)


if __name__ == "__main__":
	app.run(debug=True)