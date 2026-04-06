import jwt
import os
import logging
import re
from functools import wraps
from datetime import datetime, timezone, timedelta
from flask import render_template, request, jsonify, redirect, url_for, make_response, flash
from app import app, csrf
from login.validação import valida
from login.cadastrar import Usuário
from forms import LoginForm

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Determinar se está em produção
IS_PRODUCTION = os.getenv('FLASK_ENV') == 'production'


def validar_email(email):
    """Valida formato de email."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def validar_senha(senha):
    """Valida força da senha (mínimo 8 caracteres)."""
    if len(senha) < 8:
        return False, "Senha deve ter no mínimo 8 caracteres."
    if not any(char.isupper() for char in senha):
        return False, "Senha deve conter pelo menos uma letra maiúscula."
    if not any(char.isdigit() for char in senha):
        return False, "Senha deve conter pelo menos um número."
    return True, "Senha válida."


def token_required(f):
    """Decorator que exige token JWT válido."""
    @wraps(f)
    def decorated(*args, **kwargs):
        # Tenta pegar o token do cookie
        token = request.cookies.get('auth_token')
        if not token:
            logger.warning("Tentativa de acesso sem token")
            return jsonify({"message": "Token de autenticação é necessário!"}), 401
        try:
            # Tenta decodificar o token usando a SECRET KEY
            data = jwt.decode(
                token,
                app.config['JWT_SECRET_KEY'],
                algorithms=["HS256"]
            )
            # Armazena os dados do usuário para usar nas próximas funções
            request.user_data = data
        except jwt.ExpiredSignatureError:
            logger.warning(f"Token expirado para usuário: {request.cookies.get('auth_token')[:20]}...")
            return jsonify({"message": "Token de autenticação expirado! Faça login novamente."}), 401
        except jwt.InvalidTokenError:
            logger.warning("Token inválido detectado")
            return jsonify({"message": "Token de autenticação inválido!"}), 401
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def home():
    """Rota inicial - redireciona para HelpClinic se autenticado, senão para login."""
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
            # Token expirado, remover cookie e redirecionar para login
            logger.info("Token expirado. Removendo cookie e redirecionando para login.")
            response = make_response(redirect(url_for('inicio')))
            response.delete_cookie('auth_token')
            flash('Sua sessão expirou. Por favor, faça login novamente.')
            return response
        except jwt.InvalidTokenError:
            # Token inválido, remover cookie e redirecionar para login
            logger.warning("Token inválido detectado. Removendo cookie e redirecionando.")
            response = make_response(redirect(url_for('inicio')))
            response.delete_cookie('auth_token')
            flash('Sua sessão é inválida. Por favor, faça login novamente.')
            return response

    return redirect(url_for('inicio'))


@app.route('/login', methods=['GET', 'POST'])
def inicio():
    """Rota de login - autentica usuário e cria token JWT."""
    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)

    # Método POST - processa o formulário
    usuário = request.form.get('email', '').strip()
    senha = request.form.get('senha', '').strip()
    remember = request.form.get('remember') == 'on'

    # Validar entrada
    if not usuário or not senha:
        flash('Email e senha são obrigatórios.')
        logger.warning("Tentativa de login sem email ou senha")
        return redirect(url_for('inicio'))

    if not validar_email(usuário):
        flash('Formato de email inválido.')
        logger.warning(f"Email inválido: {usuário}")
        return redirect(url_for('inicio'))

    # Validar usuário no banco
    try:
        if not valida(usuário, senha):
            flash('Email ou senha incorretos.')
            logger.warning(f"Falha de autenticação para email: {usuário}")
            return redirect(url_for('inicio'))
    except Exception as e:
        logger.error(f"Erro ao validar usuário {usuário}: {str(e)}")
        flash('Erro ao processar login. Tente novamente.')
        return redirect(url_for('inicio'))

    # Criar token JWT
    expires_delta = timedelta(days=30) if remember else timedelta(hours=24)
    max_age = 30 * 24 * 60 * 60 if remember else 24 * 60 * 60

    try:
        now = datetime.now(timezone.utc)
        payload = {
            'email': usuário,
            'iat': now.timestamp(),
            'exp': (now + expires_delta).timestamp()
        }
        token = jwt.encode(payload, app.config['JWT_SECRET_KEY'], algorithm='HS256')

        response = make_response(redirect(url_for('HelpClinic')))
        response.set_cookie(
            'auth_token',
            token,
            max_age=max_age,
            httponly=True,
            samesite='Lax',
            secure=IS_PRODUCTION
        )

        mensagem = 'Usuário autenticado com "Lembrar-me" ativado, válido por 30 dias.' if remember else 'Usuário autenticado, válido por 24 horas.'
        flash(mensagem)
        logger.info(f"Usuário {usuário} autenticado com sucesso")

        return response
    except Exception as e:
        logger.error(f"Erro ao criar token JWT para {usuário}: {str(e)}")
        flash('Erro ao processar autenticação. Tente novamente.')
        return redirect(url_for('inicio'))


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Rota de cadastro - cria novo usuário no banco."""
    if request.method == 'GET':
        return render_template('cadastro.html')

    try:
        usuário = request.form.get('email', '').strip()
        senha1 = request.form.get('senha1', '').strip()
        senha2 = request.form.get('senha2', '').strip()

        # Validação básica
        if not usuário or not senha1 or not senha2:
            flash('Todos os campos são obrigatórios.')
            logger.warning("Tentativa de cadastro com campos vazios")
            return render_template('cadastro.html')

        # Validar email
        if not validar_email(usuário):
            flash('Email inválido. Use um formato correto (ex: usuario@email.com).')
            logger.warning(f"Email inválido no cadastro: {usuário}")
            return render_template('cadastro.html')

        # Validar senhas iguais
        if senha1 != senha2:
            flash('As senhas não correspondem.')
            logger.warning(f"Senhas diferentes no cadastro para: {usuário}")
            return render_template('cadastro.html')

        # Validar força da senha
        senha_valida, mensagem = validar_senha(senha1)
        if not senha_valida:
            flash(mensagem)
            logger.warning(f"Senha fraca no cadastro para: {usuário}")
            return render_template('cadastro.html')

        # Criar novo usuário
        novo = Usuário(usuário, senha1)
        novo.inserir_banco()

        flash('Cadastro realizado com sucesso! Faça login para continuar.')
        logger.info(f"Novo usuário cadastrado: {usuário}")
        return redirect(url_for('inicio'))

    except ValueError as e:
        # Email já existe
        flash(str(e))
        logger.warning(f"Erro de validação no cadastro: {str(e)}")
        return render_template('cadastro.html')
    except Exception as e:
        logger.error(f"Erro ao cadastrar usuário: {str(e)}")
        flash(f'Erro ao realizar cadastro: {str(e)}')
        return render_template('cadastro.html')


@app.route('/HelpClinic')
@token_required
def HelpClinic():
    """Rota principal da aplicação - requer autenticação."""
    try:
        # request.user_data foi definido no decorator token_required
        email = request.user_data['email']

        # Pega quando o token foi criado e quando expira
        # iat e exp já são timestamps Unix (números)
        # Converte para hora local (usa astimezone() sem argumentos)
        iat = datetime.fromtimestamp(request.user_data['iat']).astimezone()
        exp = datetime.fromtimestamp(request.user_data['exp']).astimezone()

        # Tempo restante (em hora UTC para cálculo correto)
        agora = datetime.now(timezone.utc)
        exp_utc = datetime.fromtimestamp(request.user_data['exp'], tz=timezone.utc)
        tempo_restante = exp_utc - agora

        # Formata tempo restante de forma legível (HH:MM:SS)
        horas, resto = divmod(int(tempo_restante.total_seconds()), 3600)
        minutos, segundos = divmod(resto, 60)
        tempo_formatado = f"{horas:02d}h {minutos:02d}m {segundos:02d}s"

        return render_template('site.html',
                          email=email,
                          token_info={
                              'criado_em': iat.strftime('%d/%m/%Y %H:%M:%S'),
                              'expira_em': exp.strftime('%d/%m/%Y %H:%M:%S'),
                              'tempo_restante': tempo_formatado
                          })
    except Exception as e:
        logger.error(f"Erro ao carregar página HelpClinic: {str(e)}")
        flash('Erro ao carregar a página. Por favor, faça login novamente.')
        return redirect(url_for('inicio'))


@app.route('/logout', methods=['POST'])
@token_required
def logout():
    """Rota para realizar logout - remove cookie de autenticação."""
    try:
        email = request.user_data.get('email', 'Usuário desconhecido')
        response = make_response(redirect(url_for('inicio')))
        response.delete_cookie('auth_token')
        flash('Você foi desconectado com sucesso!')
        logger.info(f"Usuário {email} realizou logout")
        return response
    except Exception as e:
        logger.error(f"Erro ao realizar logout: {str(e)}")
        flash('Erro ao desconectar. Por favor, tente novamente.')
        return redirect(url_for('HelpClinic'))


# Handler para erros
@app.errorhandler(404)
def not_found(error):
    """Tratamento de página não encontrada."""
    logger.warning(f"Página não encontrada: {request.url}")
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Tratamento de erro interno do servidor."""
    logger.error(f"Erro interno do servidor: {str(error)}")
    return render_template('500.html'), 500
