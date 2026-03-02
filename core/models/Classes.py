from core.models.listas import agendamentos

# Definição da classe Pacientes e o que cada um deles possui
class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

# Definição da classe Consulta e o que é necessário que cada uma tenha
class Consulta(Paciente):
    def __init__(self, nome, telefone, data):
        super().__init__(nome, telefone)
        self.data = data