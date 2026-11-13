import os
from flask import Flask

app = Flask(__name__)

# Путь к файлу внутри контейнера
DATA_FILE = '/data/counter.txt'

def get_visits():
    # Если папки /data нет, создаем её (на случай если том не примонтирован)
    os.makedirs('/data', exist_ok=True)
    if not os.path.exists(DATA_FILE):
        return 0
    with open(DATA_FILE, 'r') as f:
        return int(f.read().strip())

def save_visits(count):
    with open(DATA_FILE, 'w') as f:
        f.write(str(count))

@app.route('/')
def hello():
    visits = get_visits() + 1
    save_visits(visits)
    return f"Привет! Это мое приложение. Количество посещений: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
