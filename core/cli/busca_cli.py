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
              f'Nome: {these[0].nome}\n'
              f'Idade: {these[0].idade}\n'
              f'Telefone: {these[0].telefone}\n')
    elif len(these) > 1:
        while True:
            print(f'\n{len(these)} resultados encontrados!\n')
            for index, pac in enumerate(these, start=1):
                print(f'{index}. {pac.nome}')

            resp = input('\nQual está procurando? Digite um nome que o outro não tenha ou o nome completo de um.\n'
            'Resposta: ').strip()
            if not resp:
                print('Por favor, digite algo')
                continue
            for pac in these:
                if resp.lower() in pac.nome.lower():
                    resp = pac
                    print('\nAqui estão as informações do paciente:\n'
                        f'Nome: {resp.nome}\n'
                        f'Idade: {resp.idade}\n'
                        f'Telefone: {resp.telefone}\n')
                    break
                else:
                    print('Algo deu errado, tente novamente')
                    continue
        
    else:
        print('\nPaciente não encontrado, verifique se o nome foi escrito corretamente ou cadastre o paciente primeiro.\n')

    these.clear()