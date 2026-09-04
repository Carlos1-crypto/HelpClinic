# Dados do banco de dados e funções de conexão

import os
import mysql.connector
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)

# Variáveis globais para conexão e cursor
_conexao = None
_cursor = None


def get_conexao():
    """Estabelece conexão com o banco de dados usando variáveis de ambiente."""
    global _conexao

    try:
        _conexao = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
        )
        logger.info('Conexão com banco de dados estabelecida com sucesso.')
        return _conexao
    except mysql.connector.Error as erro:
        logger.error(f'Erro na conexão com banco de dados: {erro}')
        raise ValueError(f'Erro na conexão: {erro}')
    except Exception as erro:
        logger.error(f'Erro inesperado ao conectar ao banco de dados: {erro}')
        raise ValueError(f'Erro inesperado na conexão: {erro}')


def get_cursor():
    """Obtém o cursor da conexão, criando uma nova conexão se necessário."""
    global _conexao, _cursor

    try:
        # Se não há conexão ou está fechada, criar nova
        if _conexao is None or not _conexao.is_connected():
            _conexao = get_conexao()

        if _cursor is None:
            _cursor = _conexao.cursor()

        return _cursor
    except Exception as erro:
        logger.error(f'Erro ao obter cursor: {erro}')
        # Tentar reconectar
        _conexao = get_conexao()
        _cursor = _conexao.cursor()
        return _cursor


# Lazy initialization - não conectar até ser necessário
# Fazer assim evita que o app quebre se o banco não estiver disponível na inicialização
conexao = None
cursor = None

def inicializar_conexao():
    """Inicializa conexão e cursor quando necessário."""
    global conexao, cursor
    if conexao is None or not conexao.is_connected():
        conexao = get_conexao()
        cursor = get_cursor()
    return conexao, cursor