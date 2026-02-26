from core.services.busca import procura
from core.models.listas import these

# Bloco de código que busca pacientes por nome
def busca():
    print('\n=== Busca de Paciente ===\n')
    paciente = input('Qual é o nome do paciente que está procurando?\n'
                    'Paciente: ')
    
    while not paciente.replace(' ', '').isalpha():
        print('Nome inválido! Digite apenas letras.')
        paciente = input('Qual é o nome do paciente que está procurando?\n'
                    'Paciente: ')
    procura(paciente)
    
    # Informa o nome, idade e telefone dos pacientes que foram cadastrados no sistema, porém se não encontrado informa ao usuário
    if len(these) == 1:
        print('\nAqui estão as informações do paciente:\n'
              f'Nome: {paciente.nome}\n'
              f'Idade: {paciente.idade}\n'
              f'Telefone: {paciente.telefone}\n')
    elif len(these) > 1:
        print(f'\n{len(these)} encontrados!\n')
        for index, pac in enumerate(these, start=1):
            print(f'{index}. {pac}')
        
        while True:
            resp = input('Qual está procurando? Digite um nome que o outro não tenha ou o nome completo de um.')
            for pac in these:
                if resp.lower() in pac.nome.lower():
                    resp = pac
                    print('\nAqui estão as informações do paciente:\n'
                        f'Nome: {resp.nome}\n'
                        f'Idade: {resp.idade}\n'
                        f'Telefone: {resp.telefone}\n')

        
    else:
        print('\nPaciente não encontrado, verifique se o nome foi escrito corretamente ou cadastre o paciente primeiro.\n')

    these.clear()