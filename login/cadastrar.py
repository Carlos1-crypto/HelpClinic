from DB_data import inicializar_conexao
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
            conexao, cursor = inicializar_conexao()

            senha_criptografada = self.criptografar(self.password)
            # bcrypt.hashpw() retorna bytes, converter para string para armazenar
            senha_str = senha_criptografada.decode('utf-8')
            cursor.execute(
                """INSERT INTO usuarios (email, senha) VALUES (%s, %s)""",
                (self.user, senha_str)
            )
            conexao.commit()
            print(f"Usuário {self.user} cadastrado com sucesso!")
        except cursor.Error as erro:
            conexao.rollback()
            # Verificar se é erro de email duplicado
            if 'Duplicate entry' in str(erro) or 'UNIQUE constraint' in str(erro).upper():
                raise ValueError(f"Email {self.user} já está cadastrado no sistema.")
            raise ValueError(f"Erro ao cadastrar usuário: {erro}")
        except Exception as erro:
            conexao.rollback()
            raise ValueError(f"Erro inesperado ao cadastrar usuário: {erro}")