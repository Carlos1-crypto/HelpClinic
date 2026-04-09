from core.models.listas import agendamentos
from dataclasses import dataclass

# Definição da classe Pacientes e o que cada um deles possui
@dataclass
class Paciente:
    __slots__ = ["nome", "idade", "telefone"]
    nome: str
    idade: int
    telefone: str

# Definição da classe Consulta e o que é necessário que cada uma tenha
@dataclass
class Consulta(Paciente):
    __slots__ = ["nome", "idade", "telefone", "data"]
    data: str