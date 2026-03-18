from main import app
from flask import render_template, request, flash, redirect, url_for
from login.validação import valida
from login.cadastrar import Usuário

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')

    usuário = request.form.get('usuário')
    senha1 = request.form.get('senha1')
    senha2 = request.form.get('senha2')
    if senha1 == senha2:
        novo = Usuário(usuário, senha1)
    try:
        novo.inserir_banco()
        flash("Cadastro realizado com sucesso!")
        return render_template('login.html')
    except:
        flash("Opa, algo deu errado.")
        return render_template('cadastro.html')

@app.route('/acesso', methods=['POST'])
def site():
    usuário = request.form.get('Usuário')
    senha = request.form.get('Senha')
    if valida(usuário, senha):
        flash("Login feito com sucesso.")
        return render_template('site.html')
    else:
        flash("Nome de usuário ou senha incorretos.")
        return render_template('login.html')