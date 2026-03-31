import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_conexao():
    """Estabelece conexão com o banco de dados usando variáveis de ambiente."""
    try:
        conexao = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'c4rl05'),
            database=os.getenv('DB_NAME', 'helpclinic'),
        )
        print('Conexão bem sucedida.')
        return conexao
    except mysql.connector.Error as erro:
        raise ValueError(f'Erro na conexão: {erro}')

# Inicializar conexão e cursor global
conexao = get_conexao()
cursor = conexao.cursor()