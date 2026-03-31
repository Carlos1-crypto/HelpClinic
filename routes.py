from main import app
from flask import render_template, request, redirect, url_for
from login.validação import valida
from login.cadastrar import Usuário

@app.route('/')
def inicio():
    usuário = request.args.get('usuário')
    senha = request.args.get('senha')
    if usuário and senha:
        if valida(usuário, senha):
            return redirect(url_for('HelpClinic'))
        else:
            print('ERRO: Usuário ou senha inválidos.')
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
                return redirect(url_for('inicio'))
            except:
                print("ERRO: Cadastro não realizado.")
                return render_template('cadastro.html')
        else:
            print('ERRO: Senha diferentes.')
            return render_template('cadastro.html')
    else:
        print('ERRO: Alguma senha não digitada.')
        return render_template('cadastro.html')
    
@app.route('/HelpClinic')
def HelpClinic():
    return render_template('site.html')