from flask import *
import sqlite3 as sql

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)

    db.row_factory = sql.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def execute(query, args):
    db = get_db()
    db.execute(query, args)
    db.commit()

@app.route("/")
def index():

    pessoas = query_db("SELECT * FROM pessoa")
        
    return render_template('index.html', pessoas=pessoas)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    try:

        execute("INSERT INTO pessoa (fname,lname) VALUES (?,?)", (fname,lname))

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

@app.route('/editar', methods=['GET'])
def editar():
    id = request.args.get('id')
    pessoa = query_db("SELECT * FROM pessoa WHERE id = ?", id, one=True)

    return render_template('edit.html', pessoa=pessoa)

@app.route('/atualizar', methods=['POST'])
def atualizar():

    id = request.form.get('id')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    try:

        execute("UPDATE pessoa SET fname = ?, lname = ? WHERE id = ?", (fname,lname,id))

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

@app.route('/deletar', methods=['POST'])
def deletar():

    id = request.form.get('id')

    try:

        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("DELETE FROM pessoa WHERE id = ?", id)
            con.commit()

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

if __name__ == "__main__":
    app.debug = True
    app.run()