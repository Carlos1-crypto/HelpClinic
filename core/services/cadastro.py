<<<<<<< HEAD
from core.models.Classes import Paciente
from core.models.listas import pacientes

# Bloco de código com as regras de cadastro de novos pacientes e suas informações
def cadastrar(nome: str, idade: int, telefone: int):
    if not nome.replace(' ', '').isalpha():
        raise ValueError('Nome inválido')
    
    if idade <= 0:
        raise ValueError('Idade inválida')
    
    if telefone <= 0:
        raise ValueError('Telefone inválido')
    
    novo = Paciente(nome, idade, telefone)
    pacientes.append(novo)
    
=======
from core.models.Classes import Paciente
from core.models.listas import pacientes

# Bloco de código com as regras de cadastro de novos pacientes e suas informações
def cadastrar(nome: str, idade: int, telefone: int):
    if not nome.replace(' ', '').isalpha():
        raise ValueError('Nome inválido')
    
    if idade <= 0:
        raise ValueError('Idade inválida')
    
    if telefone <= 0:
        raise ValueError('Telefone inválido')
    
    novo = Paciente(nome, idade, telefone)
    pacientes.append(novo)
    
>>>>>>> 68d5e56a6b2bddfafb336fdda378298995c3ceab
    return novo