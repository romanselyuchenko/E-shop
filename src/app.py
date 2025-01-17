from flask import Flask, render_template
import sqlite3
import time

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            image TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', products=products, time=time.time())

if __name__ == '__main__':
    init_db()  # Инициализация базы данных
    app.run(debug=True)
