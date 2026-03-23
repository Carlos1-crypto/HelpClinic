from main import app
from flask import render_template, request, flash, redirect, url_for
from login.validação import valida
from login.cadastrar import Usuário

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')
    usuário = request.form.get('usuário')
    senha1 = request.form.get('senha1')
    senha2 = request.form.get('senha2')
    if senha1 and senha2:
        if senha1 == senha2:
            novo = Usuário(usuário, senha1)
            try:
                novo.inserir_banco()
                print("Cadastro realizado com sucesso!")
                return redirect(url_for('login'))
            except:
                print("ERRO: Cadastro não realizado.")
                return render_template('cadastro.html')
        else:
            print('ERRO: Senha diferentes.')
            return render_template('cadastro.html')
    else:
        print('ERRO: Alguma senha não digitada.')
        return render_template('cadastro.html')


@app.route('/acesso', methods=['POST'])
def site():
    render_template('site.html')