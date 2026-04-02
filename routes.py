import jwt
import os
from main import app
from flask import render_template, request, jsonify, redirect, url_for, make_response, flash
from login.validação import valida
from login.cadastrar import Usuário
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', app.config['SECRET_KEY'])

if not app.config['SECRET_KEY'] or app.config['JWT_SECRET_KEY'] == 'default_secret_key':
    raise ValueError("ATENÇÃO, você está usando uma chave insegura! As chaves SECRET_KEY e JWT_SECRET_KEY devem ser definidas no arquivo .env")

def token_required(f):
    def decorated(*args, **kwargs):
        # Tenta pegar o token do cookie
        token = request.cookies.get('auth_token')
        if not token:
            return jsonify({"message": "Token de autenticação é necessário!"}), 401
        try:
            # Tenta decodificar o token usando a SECRET KEY
            # Se falhar, significa que o token é inválido ou foi alterado
            data = jwt.decode(
                token,
                app.config['JWT_SECRET_KEY'],
                algorithms=["HS256"]
                )
            # Armazena os dados do usuário para usar nas próximas funções
            request.user_data = data
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token de autenticação expirado! Faça login novamente."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token de autenticação inválido!"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def home():
    token = request.cookies.get('auth_token')
    # Verifica se o token ainda é válido
    if token:
        try:
            jwt.decode(
                token,
                app.config['JWT_SECRET_KEY'],
                algorithms=["HS256"]
                )
            return redirect(url_for('HelpClinic'))
        except jwt.ExpiredSignatureError:
            # Token inválido, mostra página de login
            print("Token expirado. Redirecionando para login.")
            pass
        except jwt.InvalidTokenError:
            # Token inválido, mostra página de login
            print("Token inválido. Redirecionando para login.")
            pass
    return redirect(url_for('inicio'))

@app.route('/login', methods=['GET', 'POST'])
def inicio():
    if request.method == 'GET':
        return render_template('login.html')

    # Método POST - processa o formulário
    usuário = request.form.get('email')
    senha = request.form.get('senha')
    remember = request.form.get('remember') == 'on'

    if not usuário or not senha:
        flash('Email e senha são obrigatórios.')
        return redirect(url_for('inicio'))

    if not valida(usuário, senha):
        flash('Email ou senha incorretos.')
        return redirect(url_for('inicio'))

    expires_delta = timedelta(days=30) if remember else timedelta(hours=24)
    max_age = 30 * 24 * 60 * 60 if remember else 24 * 60 * 60
    mensagem = 'Usuário autenticado com "Lembrar-me" ativado, válido por 30 dias.' if remember else 'Usuário autenticado, válido por 24 horas.'

    payload = {
        'email': usuário,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + expires_delta
    }
    token = jwt.encode(payload, app.config['JWT_SECRET_KEY'], algorithm='HS256')

    response = make_response(redirect(url_for('HelpClinic')))
    response.set_cookie('auth_token', token, max_age=max_age, httponly=True, samesite='Lax', secure=False)
    flash(mensagem)
    return response


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
@token_required # Este decorator exige que o usuário esteja autenticado
def HelpClinic():
    # request.user_data foi definido no decorator token_required
    email = request.user_data['email']

    # Pega quando o token foi criado e quando expira
    iat = datetime.fromtimestamp(request.user_data['iat'])
    exp = datetime.fromtimestamp(request.user_data['exp'])

    return render_template('site.html', 
                      email=email, 
                      token_info={
                          'criado_em': iat.strftime('%d/%m/%Y %H:%M:%S'),
                          'expira_em': exp.strftime('%d/%m/%Y %H:%M:%S'),
                          'tempo_restante': str(exp - datetime.utcnow())
                      })