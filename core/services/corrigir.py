from core.models.listas import pacientes

errados = ['nome', 'idade', 'telefone']

def loop():
    while True:
            resp = input('Há outra informação do paciente que você gostaria de atualizar?\n' \
                        '1. Não\n'
                        '2. Sim\n'
                        'Resposta: ')
            match resp.lower():
                case 'não':
                    break
                case 'sim':
                    num = 1
                    for e in errados:
                        print(f'{num}. {e}')
                        num += 1
                    escolha = input('Resposta: ')

                    for i in errados:
                        if escolha == i:
                            escolha = i
                        match escolha.lower():
                            case 'nome':
                                update = input(f'Nome antigo: {escolha}\n'
                                                'Atualização: ')
                                escolha = update
                                errados.remove('nome')
                                print('Alteração realizada com sucesso.')
                                break
                            case 'idade':
                                update = input(f'Idade antiga: {escolha}\n'
                                                'Atualização: ')
                                escolha = update
                                errados.remove('idade')
                                print('Alteração realizada com sucesso.')
                                break
                            case 'telefone':
                                update = input(f'Telefone antigo: {escolha}\n'
                                                'Atualização: ')
                                escolha = update
                                errados.remove('telefone')
                                print('Alteração realizada com sucesso.')
                                break
                            case _:
                                print("Opção inválida!\n")
                case _:
                    print('Opção inválida!\n')

def corrigir():
    print('\n=== Correção de Cadastro ===\n')
    for i, pac in enumerate(pacientes, 1):
        print(f'{i}. {pac.nome}')
    procura = input('\nQual é o nome do paciente que está procurando?\n'
    'Paciente: ')

    encontrado = False
    for pac in pacientes:
        if procura.lower() in pac.nome.lower():
            encontrado = pac

    if encontrado:
        while True:
            resp = input('\nAqui estão as informações do paciente:\n'
                f'Nome: {encontrado.nome}\n'
                f'Idade: {encontrado.idade}\n'
                f'Telefone: {encontrado.telefone}\n'
                'Qual informação você gostaria de atualizar?\n'
                'Resposta: ')
            match resp.lower():
                case 'nome':
                    update = input(f'Nome antigo: {encontrado.nome}\n'
                                    'Atualização: ')
                    encontrado.nome = update
                    errados.remove('nome')
                    print('Alteração realizada com sucesso.')
                    break
                case 'idade':
                    update = input(f'Idade antiga: {encontrado.idade}\n'
                                    'Atualização: ')
                    encontrado.idade = update
                    errados.remove('idade')
                    print('Alteração realizada com sucesso.')
                    break
                case 'telefone':
                    update = input(f'Telefone antigo: {encontrado.telefone}\n'
                                    'Atualização: ')
                    encontrado.telefone = update
                    errados.remove('telefone')
                    print('Alteração realizada com sucesso.')
                    break
                case _:
                    print("Opção inválida!\n")
        loop()
    else:
        print('\nPaciente não encontrado, verifique se o nome foi escrito corretamente ou cadastre o paciente primeiro.\n')
