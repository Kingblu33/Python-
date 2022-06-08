from http.client import REQUEST_ENTITY_TOO_LARGE
from winreg import QueryInfoKey
from xml.dom.minidom import Identified
from flask_app import app
from flask import render_template,session,redirect,request
from flask_app.models.painting_model import Painting
from flask import flash



@app.route('/painting/new')
def newpainting():


    return render_template('addpainting.html')


@app.route('/addpainting',methods=['post'])
def addingnewpainting():

    if not  Painting.validate_paintings(request.form):
        return redirect('/painting/new')
    query_data={
    "title":request.form['title'],
    "description":request.form['description'],
    "price":int(request.form['price']),
    "artist_id":session['userid'],
    }

    Painting.add_painting(query_data)


    return redirect('/paintings')


@app.route('/edit/paintings/<int:id>')
def editpainting(id):
    if 'userid' not in session:
        flash("please login")
        return redirect('/')

    query= {
        "id":id
    }
    
    painting=Painting.get_one_painting(query)

    return render_template('edit.html',painting = painting)


@app.route('/editpainting/<int:id>',methods=['post'])
def updatepainting(id):
    if 'userid' not in session:
        flash("please login")
        return redirect('/')

    if not Painting.validate_paintings(request.form):
        return redirect(f'/edit/paintings/{id}')
    query={
        "id":id,
        "title":request.form['title'],
        "description":request.form['description'],
        "price":int(request.form['price']),
        "artist_id":session['userid'],
    }


    Painting.udpate_painting(query)
    return redirect('/paintings')


@app.route('/show/painting/<int:id>')
def showonepainting(id):
    if 'userid' not in session:
        flash("please login")
        return redirect('/')
    query={
        "id":id
    }
    paint=Painting.showone(query)
    return render_template('showonepainting.html',paint=paint)

@app.route('/delete/<int:id>')
def delete(id):
    if 'userid' not in session:
        flash("please login")
        return redirect('/')
    query={
        "id":id
    }
    Painting.delete_paint(query)

    return redirect('/paintings')