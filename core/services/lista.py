from core.models.listas import pacientes

def lista():
    print('\n=== Lista de Pacientes ===\n')
    num = 1
    for paciente in pacientes:
        print(f'{num}. {paciente.nome}')
        num += 1