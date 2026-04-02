"""
Configuração centralizada da aplicação Flask.
Este arquivo evita importação circular entre main.py e routes.py
"""
import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

load_dotenv()

# Inicializar Flask
app = Flask(__name__)

# Configurar segurança
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', app.config['SECRET_KEY'])

# Validar chaves de segurança
if not app.config['SECRET_KEY'] or app.config['JWT_SECRET_KEY'] == 'default_secret_key':
    raise ValueError("ATENÇÃO, você está usando uma chave insegura! As chaves SECRET_KEY e JWT_SECRET_KEY devem ser definidas no arquivo .env")

# Inicializar proteção CSRF
csrf = CSRFProtect(app)
