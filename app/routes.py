# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)
