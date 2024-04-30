from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/items')
def get_items():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="user",
        password="password",
        host="db"
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM items')
    items = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')