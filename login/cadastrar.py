from dados import cursor

class Usuário:
    def __init__(self, user, password):
        self.user = user
        self.password = password
    def inserir_banco(self):
        comando = f"""INSERT INTO Usuarios(usuário, senha) VALUES ('{self.user}', '{self.password}');"""
        cursor.execute(comando)
        cursor.commit()
        
