from DB_data import cursor
import bcrypt

def carregar_usuario(usuario):
    """Carrega um usuário específico do banco de dados."""
    consulta = "SELECT email, senha FROM usuarios WHERE email = %s;"
    cursor.execute(consulta, (usuario,))
    resultado = cursor.fetchone()
    return resultado

def valida(usuário_entrada, senha_entrada):
    try:
        # Buscar usuário no banco
        resultado = carregar_usuario(usuário_entrada)

        if resultado is None:
            # Usuário não existe
            return False

        usuario_db, hash_db = resultado

        # Comparar senha usando bcrypt
        # bcrypt.checkpw() é seguro contra timing attacks
        senha_valida = bcrypt.checkpw(
            senha_entrada.encode('utf-8'),
            hash_db.encode('utf-8')  # Se hash está em string, converter para bytes
        )

        return senha_valida

    except Exception as erro:
        print(f"Erro ao validar usuário: {erro}")
        return False