from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
# creates an instance utilizing the Flask framework and store it as 'app'
app.secret_key = "Bluebear"


@app.route('/')

def index():
    if "random_number" not in session:
        session["random_number"]= random.randint(1,100)
        print(session["random_number"])
    else:
        print(session["random_number"])

    return render_template("numba.html")

@app.route("/user",methods=["post"])
def number():
        session["input_number"] = int(request.form["number"])
        return redirect('/')


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)