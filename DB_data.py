import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_conexao():
    """Estabelece conexão com o banco de dados usando variáveis de ambiente."""
    try:
        conexao = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'db_helpclinic'),
            port=int(os.getenv('DB_PORT', 3306))
        )
        print('Conexão bem sucedida.')
        return conexao
    except mysql.connector.Error as erro:
        raise ValueError(f'Erro na conexão: {erro}')

# Inicializar conexão e cursor global
conexao = get_conexao()
cursor = conexao.cursor()