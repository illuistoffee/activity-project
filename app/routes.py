from flask import Flask, render_template
from app import myapp_obj
from app import forms
# different URL the app will implement

@myapp_obj.route("/")
# called view function
def hello():
   user = {'username': 'doof'}
   return render_template('index.html',title='Home',user=user) 

@myapp_obj.route("/login")
def login():
   form = LoginForm()
   return render_template('login.html',title='Sign In',form=form)

@myapp_obj.route("/listings")
def listings():
   return 'Work in Progress.'

@myapp_obj.route("/listings/<string:ID>")
def listingsID():
   return ID 



