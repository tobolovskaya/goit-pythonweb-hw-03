from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join("storage", "data.json")

if not os.path.exists("storage"):
    os.makedirs("storage")

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({}, file)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("message")

        if username and message:
            
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            data[str(datetime.now())] = {"username": username, "message": message}

            with open(DATA_FILE, "w") as file:
                json.dump(data, file, indent=4)

            return redirect(url_for("index"))

    return render_template("message.html")


@app.route("/read")
def read():
    with open(DATA_FILE, "r") as file:
        messages = json.load(file)
    return render_template("read.html", messages=messages)


@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(port=3000, debug=True)
