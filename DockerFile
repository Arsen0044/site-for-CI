# Використовуємо офіційний образ Python 3.12 як базовий
FROM python:3.12-slim

# Встановлюємо робочий каталог в контейнері
WORKDIR /app

# Копіюємо файл вимог (requirements.txt) в контейнер
COPY requirements.txt .

# Встановлюємо залежності (в тому числі Flask)
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код програми в контейнер
COPY . .

# Відкриваємо порт 5000 для доступу до Flask додатку
EXPOSE 5000

# Визначаємо команду для запуску Flask додатку
CMD ["python", "app.py"]
