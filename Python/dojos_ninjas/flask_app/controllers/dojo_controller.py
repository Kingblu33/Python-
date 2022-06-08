from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo_model import Dojo

@app.route('/')
def re():
    return redirect('/create/dojo')

@app.route('/show/dojos')
def showdojo():
    return render_template('createdojo.html')

@app.route('/create/dojo', methods=["POST"])
def newdojo():
    data = {
        "name" : request.form['name']
    } 
    dojos = Dojo.savedojo(data)
    return redirect('/show/dojos',dojos=dojos)