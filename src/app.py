from flask import Flask, jsonify
import sqlite3

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
    return "Hola!"

@app.route('/products')
def get_products():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    
    # Форматируем данные для ответа
    product_list = []
    for product in products:
        product_list.append({
            "id": product[0],
            "name": product[1],
            "price": product[2],
            "image": product[3]
        })
    
    return jsonify(product_list)

if __name__ == '__main__':
    init_db()  # Инициализация базы данных
    app.run(debug=True)
