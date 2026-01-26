from core.models.listas import agendamentos

# Definição da classe Pacientes e o que cada um deles possui
class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
    def agendar(self, data):
        consulta = Consulta(self.nome, data)
        agendamentos.append(consulta)

# Definição da classe Consulta e o que é necessário que cada uma tenha
class Consulta:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data