from core.models.listas import pacientes

these = []

# Bloco de código que busca pacientes por nome
def busca():
    print('\n=== Busca de Paciente ===\n')
    procura = input('Qual é o nome do paciente que está procurando?\n'
                    'Paciente: ')
    
    # Logo após o nome do paciente ser informado pelo o usuário, o sistema procura pelo nome dele colocando as letras digitadas na busca e as letras digitadas na
    # hora do cadastro para ver se há alguem com esse nome
    for paciente in pacientes:
        if procura.lower() in paciente.nome.lower():
            these.append(paciente)
    
    # Informa o nome, idade e telefone dos pacientes que foram cadastrados no sistema, porém se não encontrado informa ao usuário
    if len(these) == 1:
        print('\nAqui estão as informações do paciente:\n'
              f'Nome: {paciente.nome}\n'
              f'Idade: {paciente.idade}\n'
              f'Telefone: {paciente.telefone}\n')
    elif len(these) > 1:
        resp = input(f'\n{len(these)} encontrados! Qual está procurando?\n')
        num = 1
        for pac in these:
            print(f'{num}. {pac.nome}')
            num += 1
        for pac in these:
            if resp.lower() in pac.nome.lower():
                resp = pac
                print('\nAqui estão as informações do paciente:\n'
                    f'Nome: {resp.nome}\n'
                    f'Idade: {resp.idade}\n'
                    f'Telefone: {resp.telefone}\n')

        
    else:
        print('\nPaciente não encontrado, verifique se o nome foi escrito corretamente ou cadastre o paciente primeiro.\n')
