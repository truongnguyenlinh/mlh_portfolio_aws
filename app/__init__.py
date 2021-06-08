import os
from flask import Flask, render_template, send_from_directory


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

    return app
