from core.services.busca import procura
<<<<<<< HEAD
=======
from core.models.listas import these
>>>>>>> 68d5e56a6b2bddfafb336fdda378298995c3ceab

# Bloco de código que busca pacientes por nome
def busca():
    print('\n=== Busca de Paciente ===\n')
    paciente = input('Qual é o nome do paciente que está procurando?\n'
                    'Paciente: ')
<<<<<<< HEAD
    procura(paciente)
    
    # Logo após o nome do paciente ser informado pelo o usuário, o sistema procura pelo nome dele colocando as letras digitadas na busca e as letras digitadas na
    # hora do cadastro para ver se há alguem com esse nome
    for paciente in pacientes:
        if procura.lower() in paciente.nome.lower():
            these.append(paciente)
    
    # Informa o nome, idade e telefone dos pacientes que foram cadastrados no sistema, porém se não encontrado informa ao usuário
    if len(these):
=======
    
    while not paciente.replace(' ', '').isalpha():
        print('Nome inválido! Digite apenas letras.')
        paciente = input('Qual é o nome do paciente que está procurando?\n'
                    'Paciente: ')
    procura(paciente)
    
    # Informa o nome, idade e telefone dos pacientes que foram cadastrados no sistema, porém se não encontrado informa ao usuário
    if len(these) == 1:
>>>>>>> 68d5e56a6b2bddfafb336fdda378298995c3ceab
        print('\nAqui estão as informações do paciente:\n'
              f'Nome: {paciente.nome}\n'
              f'Idade: {paciente.idade}\n'
              f'Telefone: {paciente.telefone}\n')
    elif len(these) > 1:
<<<<<<< HEAD
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
=======
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
>>>>>>> 68d5e56a6b2bddfafb336fdda378298995c3ceab

        
    else:
        print('\nPaciente não encontrado, verifique se o nome foi escrito corretamente ou cadastre o paciente primeiro.\n')
<<<<<<< HEAD
=======

    these.clear()
>>>>>>> 68d5e56a6b2bddfafb336fdda378298995c3ceab
