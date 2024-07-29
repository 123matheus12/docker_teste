from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = psycopg2.connect(
        host="db",
        database="postgres",
        user="postgres",
        password="example"
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return f'Hello, World! Database version: {db_version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
