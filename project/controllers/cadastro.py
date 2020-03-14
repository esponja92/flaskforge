from project import app
from flask import render_template, redirect, url_for, request
from project.models.pessoa import Pessoa


@app.route("/")
def index():

    pessoas = Pessoa().obter()
        
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
    pessoa = Pessoa().obterPorId(id)

    return render_template('edit.html', pessoa=pessoa)

@app.route('/atualizar', methods=['POST'])
def atualizar():

    id = request.form.get('id')
    fname = request.form.get('fname')
    lname = request.form.get('lname')

    try:
        pessoa = Pessoa()
        pessoa.campo_id = id
        pessoa.campo_fname = fname
        pessoa.campo_lname = lname
        pessoa.atualizar()

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))

@app.route('/deletar', methods=['POST'])
def deletar():

    id = request.form.get('id')

    try:

        pessoa = Pessoa().obterPorId(id)
        pessoa.deletar()

        return render_template('sucesso.html')
    except Exception as e:
        return render_template('erro.html', erro=str(e))
