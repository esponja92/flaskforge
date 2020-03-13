from project import app
from flask import render_template, redirect, url_for, request
from project.repository.database_pessoa import DatabasePessoa
from project.models.pessoa import Pessoa

db = DatabasePessoa()

@app.route("/")
def index():

    pessoas = db.obtem()
        
    return render_template('index.html', pessoas=pessoas)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    try:
        pessoa = Pessoa()
        pessoa.campo_fname = fname
        pessoa.campo_lname = lname
        pessoa.criar()

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

@app.route('/editar', methods=['GET'])
def editar():
    id = request.args.get('id')
    pessoa = db.obtem(colunas="*", where_colunas=['id'], where_valores=[id], one=True)

    return render_template('edit.html', pessoa=pessoa)

@app.route('/atualizar', methods=['POST'])
def atualizar():

    id = request.form.get('id')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    try:

        db.atualiza(['fname', 'lname'], [fname, lname],['id'], [id])

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

@app.route('/deletar', methods=['POST'])
def deletar():

    id = request.form.get('id')

    try:

        db.deleta(where_colunas = ["id"], where_valores = [id])

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))
'''
if __name__ == "__main__":
    app.debug = True
    app.run()
'''
