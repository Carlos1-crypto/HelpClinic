from core.models.listas import pacientes
from core.models.listas import these

# Bloco de código que busca pacientes por nome
def procura(paciente: str):
    
    if not paciente.replace(' ', '').isalpha():
        raise ValueError('Nome inválido')
    
    # Logo após o nome do paciente ser informado pelo o usuário, o sistema procura pelo nome dele colocando as letras digitadas na busca e as letras digitadas na
    # hora do cadastro para ver se há alguem com esse nome
    for pac in pacientes:
        if pac.nome.lower() in paciente.nome.lower():
            these.append(paciente)