from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import datetime
import json
import os

app = Flask(__name__)

# Шлях до файлу для збереження повідомлень
DATA_FILE = os.path.join("storage", "data.json")

# Створіть storage/data.json, якщо його немає
if not os.path.exists("storage"):
    os.makedirs("storage")

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump({}, file)


# Головна сторінка
@app.route("/")
def index():
    return render_template("index.html")


# Сторінка для надсилання повідомлення
@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        username = request.form.get("username")
        message = request.form.get("message")

        if username and message:
            # Збереження у файл
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            data[str(datetime.now())] = {"username": username, "message": message}

            with open(DATA_FILE, "w") as file:
                json.dump(data, file, indent=4)

            return redirect(url_for("index"))

    return render_template("message.html")


# Сторінка для читання збережених повідомлень
@app.route("/read")
def read():
    with open(DATA_FILE, "r") as file:
        messages = json.load(file)
    return render_template("read.html", messages=messages)


# Маршрут для статичних ресурсів (CSS, лого)
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)


# Обробка помилки 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(port=3000, debug=True)
