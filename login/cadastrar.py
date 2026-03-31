from DB_data import conexao, cursor
import bcrypt

class Usuário:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def criptografar(self, password):
        """Criptografa a senha usando bcrypt com salt automático."""
        salt = bcrypt.gensalt(rounds=12)  # Aumentar rounds melhora a segurança
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        return password_hash

    def inserir_banco(self):
        """Insere o usuário no banco de dados com senha criptografada."""
        try:
            senha_criptografada = self.criptografar(self.password)
            cursor.execute(
                """INSERT INTO usuarios (email, senha) VALUES (%s, %s)""",
                (self.user, senha_criptografada)
            )
            conexao.commit()
            print(f"Usuário {self.user} cadastrado com sucesso!")
        except Exception as erro:
            conexao.rollback()
            print(f"Erro ao cadastrar usuário: {erro}")