from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello Akash..</h2>'

@app.route('/puppy_latin/<name>')
def latin(name):
	if name[-1] != 'y':
		return "Your latin name is: {}".format(name + "y")

	if name[-1] == 'y':
		return "Your latin name is {}".format( name[:-1]+ "iful" )

if __name__ == '__main__':
	app.run(debug=True)