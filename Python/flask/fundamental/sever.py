from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following\
def hello_world():
    return render_template("index.html")
# import statements, maybe some other routes 
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)	

@app.route('/success')
def success():
    return "success"

@app.route('/dojo')
def dojo():
    return "dojo"
# app.run(debug=True) should be the very last statement! 
@app.route('/say/<string:name>')
def say(name):
    print(name)
    return "Hello " + name

@app.route('/repeat/<int:amount>/<string:word>')
def repeat(amount, word):

    return f"{amount*word}\n"
@app.route('/<path:path>')
def error(path):
    return "404 page not found"
# Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

