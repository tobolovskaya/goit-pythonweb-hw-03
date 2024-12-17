from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = os.path.join("storage", "data.json")

# Функція для завантаження даних з файлу
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

# Функція для збереження даних у файл
def save_data(username, message):
    data = load_data()  # Завантажуємо наявні дані
    timestamp = str(datetime.now())  # Генеруємо унікальний ключ на основі поточного часу
    data[timestamp] = {"username": username, "message": message}
    
    # Записуємо дані у файл
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Головна сторінка
@app.route("/")
def index():
    return render_template("index.html")

# Сторінка з формою
@app.route("/message", methods=["GET", "POST"])
def message():
    if request.method == "POST":
        # Отримання даних з форми
        username = request.form.get("username", "Anonymous")
        user_message = request.form.get("message", "")
        
        # Збереження даних у файл
        if user_message:
            save_data(username, user_message)
        return redirect(url_for("index"))
    return render_template("message.html")

# Обробка помилки 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

if __name__ == "__main__":
    # Переконайтеся, що папка storage існує
    if not os.path.exists("storage"):
        os.makedirs("storage")
    app.run(debug=True, port=3000)
