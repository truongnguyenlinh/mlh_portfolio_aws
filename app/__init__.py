import os
from flask import Flask, render_template, send_from_directory

# Flask uses load_dotenv by default
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route("/projects")
def carousel():
    return render_template("carousel.html", title="works", url=os.getenv("URL"))

@app.route("/about")
def about_me():
    return render_template("about_me.html", title="about_me", url=os.getenv("URL"))

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact", url=os.getenv("URL"))

@app.route("/health")
def healthy():
    return ''
