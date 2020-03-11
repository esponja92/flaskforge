from flask import *
from database import Database

app = Flask(__name__)
db = Database()

@app.route("/")
def index():

    pessoas = db.obtem('pessoa')
        
    return render_template('index.html', pessoas=pessoas)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    try:

        db.insere("pessoa", ['fname', 'lname'], [fname, lname])

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

@app.route('/editar', methods=['GET'])
def editar():
    id = request.args.get('id')
    pessoa = db.obtem('pessoa', colunas="*", where_colunas=['id'], where_valores=[id], one=True)

    return render_template('edit.html', pessoa=pessoa)

@app.route('/atualizar', methods=['POST'])
def atualizar():

    id = request.form.get('id')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    try:

        db.atualiza("pessoa", ['fname', 'lname'], [fname, lname],['id'], [id])

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

@app.route('/deletar', methods=['POST'])
def deletar():

    id = request.form.get('id')

    try:

        db.deleta('pessoa', where_colunas = ["id"], where_valores = [id])

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

if __name__ == "__main__":
    app.debug = True
    app.run()