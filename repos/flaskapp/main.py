from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello/<city>")
def hello(city):
    return f"<h1>Hello, {city}!</h1>"

@app.route("/about")
def about():
    return render_template("about.html") 

if __name__ == '__main__':
    app.run(debug=True)