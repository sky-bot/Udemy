from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, 
					RadioField, SelectField, TextField,
					TextAreaField, SubmitField) 

from wtforms.validators import DataRequired
 

app =Flask(__name__)

app.config['SECRET_KEY'] = "myKey"

class InfoForm(FlaskForm):

	breed = StringField("What breed are YOU?", validators=[DataRequired()])
	neutered = BooleanField("Have you been neutered?")
	mood = RadioField("Please choose your mood", choices=[('mood_one','Happy'),('mood_two','Excited')])
	food_choice = SelectField(u'Pick Your Fav Food: ',
								choices=[('chi','Chicken'),('bf','Beef')])
		
	submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
	form = InfoForm()

	if form.validate_on_submit():
		session['breed']=form.breed.data
		session['neutered'] = form .neutered.data
		session['mood'] = form.mood.data
		session['food'] = form.food_choice.data

		return redirect(url_for('Thank'))

	return render_template('index.html', form=form)

@app.route('/thankYou')
def Thank():
	return render_template('thankYou.html')


if __name__ == '__main__':
	app.run(debug=True)
