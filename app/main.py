# from flask import Flask
# #flask is the framwork and Flask is the python class data type
# #Flask create instances of web application


# app = Flask(__name__)


# @app.route('/')
# #function 'index' mapped to home "/" URL
# #means when we run the above code on local host: 5000/, index function will run and return output on homepage
# #if app.route was app.route('/about/'), then we have to visit : localhost:5000/about/


# def index():
#     return "Flask is working"
# '''Function index returning some string'''     

# #python assigns the name "__main__" to the script, when it is executed
# #therefore, if __name__ equals "__main__", then it will go for app.run()
# #above technique allows programmers to have control over script's behavior
# if __name__ == "__main__":
#     app.run(debug=True)
# #debug = True
# #it will print out possible python errors on the webpage

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('home.html')

if __name__ == "__main__":
	app.run(debug=True)
