from core.models.listas import pacientes

def lista():
    print('\n=== Lista de Pacientes ===\n')
    for index, paciente in enumerate(pacientes, start=1):
        print(f'{index}. {paciente.nome}')