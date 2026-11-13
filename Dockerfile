# Используем легкий базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код нашего приложения
COPY app.py .

# Указываем, что приложение слушает порт 5000
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]
