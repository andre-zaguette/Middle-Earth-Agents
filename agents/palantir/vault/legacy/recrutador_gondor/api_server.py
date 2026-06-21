from flask import Flask, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host='192.168.15.7',
        database='recrutador_gondor',
        user='gandalf',
        password='mithril_shield',
        port='5432'
    )
    return conn

@app.route('/vagas', methods=['GET'])
def get_vagas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, titulo, empresa, localizacao, link, status FROM vagas ORDER BY data_descoberta DESC;')
    vagas = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify([
        {
            "id": v[0],
            "titulo": v[1],
            "empresa": v[2],
            "localizacao": v[3],
            "link": v[4],
            "status": v[5]
        } for v in vagas
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
