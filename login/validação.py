from DB_data import inicializar_conexao
import bcrypt
import logging

logger = logging.getLogger(__name__)

def carregar_usuario(usuario):
    """Carrega um usuário específico do banco de dados."""
    try:
        conexao, cursor = inicializar_conexao()
        consulta = "SELECT email, senha FROM usuarios WHERE email = %s;"
        cursor.execute(consulta, (usuario,))
        resultado = cursor.fetchone()
        return resultado
    except Exception as erro:
        logger.error(f"Erro ao carregar usuário {usuario}: {erro}")
        return None

def valida(usuário_entrada, senha_entrada):
    """Valida credenciais do usuário."""
    try:
        # Buscar usuário no banco
        resultado = carregar_usuario(usuário_entrada)

        if resultado is None:
            # Usuário não existe
            return False

        usuario_db, hash_db = resultado

        # Comparar senha usando bcrypt
        # bcrypt.checkpw() é seguro contra timing attacks
        # hash_db vem como string do banco, converter para bytes
        if isinstance(hash_db, str):
            hash_bytes = hash_db.encode('utf-8')
        else:
            hash_bytes = hash_db

        senha_valida = bcrypt.checkpw(
            senha_entrada.encode('utf-8'),
            hash_bytes
        )

        return senha_valida

    except Exception as erro:
        logger.error(f"Erro ao validar usuário: {erro}")
        return False