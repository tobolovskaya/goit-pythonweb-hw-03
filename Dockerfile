# Використовуємо офіційний образ Python
FROM python:3.11-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файл залежностей
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо всі файли проекту в контейнер
COPY . .

# Відкриваємо порт 3000 для додатку
EXPOSE 3000

# Команда для запуску додатку
CMD ["python", "app.py"]
