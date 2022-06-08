from flask import render_template,request, redirect
from flask_app import app
from flask_app.models.dojo_model import Dojo


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/results',methods=['POST'])
def create_survey():
    if Dojo.validate_dojo(request.form):
        Dojo.createdojo(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def results():
    return render_template('checkout.html', dojo = Dojo.retrievedojo())
