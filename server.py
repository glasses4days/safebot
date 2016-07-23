from flask import Flask, render_template, redirect, request, session, jsonify
from jinja2 import StrictUndefined
from sqlalchemy import update


app = Flask(__name__)

app.secret_key = "very_very_secret"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def render_index():
    """Homepage"""

    return render_template("homepage.html")

if __name__ == "__main__":

    connect_to_db(app)

    app.run()
