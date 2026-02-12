from core.models.listas import pacientes

def informações():
    if not pacientes:
        return print('Não há pacientes cadastrados')