from itertools import count
from unicodedata import name
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    student_id=request.form["student_id"]
    fname=request.form["first_name"]
    lname=request.form["last_name"]
    val1= request.form["strawberry"]
    val2= request.form["raspberry"]
    val3= request.form["apple"]
    count=int(val1)+ int(val2) + int(val3)
    return render_template("checkout.html",student_id= student_id,fname=fname,lname=lname,count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)   