from flask import Flask, render_template
from flask_wtf import FlaskForm    #Flask form iss a classs that we inherit to create our own class
from wtforms import StringField,SubmitField    # importing fields that we use in our form

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):                      #our class Infoform inherits from Flaskform
 
	breed = StringField("What breed are You? ") 
	submit = SubmitField('Submit')

@app.route('/',methods=['GET', 'POST'])
def index():
	breed = False

	form = InfoForm()

	if(form.validate_on_submit()):

		breed = form.breed.data
		form.breed.data = " "

	return render_template('index.html',form=form,breed=breed)

if __name__ == '__main__':
	app.run(debug=True)