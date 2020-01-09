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

from flask import Flask
app = Flask(__name__)

@app.route('/')
#the above line is a decorator which binds the below function and returns some strings
def index():
	return 'Flask is working'


#how to use dyanamically
#after 'localhost:5000/profile/', pass any string and press enter
@app.route('/profile/<username>')
def profile(username):
	return "<h2> Hye %s </h2> " %username

#passing integer data type to the url
#for integer data type, we have to mention the data type here
@app.route('/post/<int:post_id>')
def post_id(post_id):
	return "<h1> <i> the post number is: %s </i> </h3>" %post_id


if __name__ == "__main__":
	app.run(debug=True)


