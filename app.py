from flask import Flask
from flask import request, jsonify
from flask import render_template
import json

app = Flask(__name__)

users = [
    {
        "username":"user",
        "password":"pass"
    }
]

@app.route("/", methods=["GET","POST"])
def login():
    return render_template('login.html')

@app.route("/registration", methods=["GET","POST"])
def registration():
    return render_template('registration.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)