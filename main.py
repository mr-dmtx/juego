from flask import Flask, render_template, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def Index():
    try:
        db = sqlite3.connect('link.db', check_same_thread=False, timeout = 10)
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        dados = db.execute("select * from link where id = 1").fetchall()
        db.close()
        return render_template("index.html", dados=dados)
    except:
        return render_template('index.html', jsonify({'msg': 'Ocorreu um erro tente novamente!'}))

@app.route('/', methods=["POST"])
def AdicionarLink():
    try:
        link = request.get_json()
        link = link["link"]
        print(link)
        db = sqlite3.connect('link.db', check_same_thread=False, timeout = 10)
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute("update link set url = ? where id = 1", (link,))
        db.commit()
        db.close()
        return jsonify({'msg': 'Link alterado!'}), 200
    except:
        return jsonify({'msg': 'Tente novamente!'}), 500

if __name__ == "__main__":
    app.run(debug=True)
