from flask import Flask , render_template, session, redirect
app = Flask(__name__)



@app.route("/")
def index():

    return render_template("index.html")


@app.route("/result")
def result():

    

    return redirect("/")






if __name__=="__main__":
    app.run(debug=True)