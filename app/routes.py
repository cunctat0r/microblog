# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index.html')
def index():
	user = {'username': 'Slava'}
	posts = [
		{
			'author': {'username': 'John Smith'},
			'body': 'What a beautiful day!'
		},
		{
			'author': {'username': 'Jane Doe'},
			'body': 'Test message'
		},
		{
			'author': {'username': 'ABBA'},
			'body': 'It\'s a rich-man-world'
		},
		{
			'author': {'username': 'Pinochet'},
			'body': 'There is a good weather in Santiago'
		},
		{
			'author': {'username': 'Che'},
			'body': 'Viva la Revolicion!'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)