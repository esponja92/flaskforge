from flask import *
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/formulario', methods=['POST'])
def formulario():
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    with sql.connect("database.db") as con:
        cur = con.cursor()

        cur.execute("INSERT INTO pessoa (fname,lname) VALUES (?,?)", (fname,lname))
        con.commit()
        
    return render_template('sucesso.html')

if __name__ == "__main__":
    app.debug = True
    app.run()