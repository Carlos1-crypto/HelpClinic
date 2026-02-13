from core.services.cadastro import cadastrar

# Bloco de código para o cadastro de novos pacientes e suas informações
def cadastro():
    print("\n=== Cadastro de Paciente ===")
    nome = input("Nome: ")
    while not nome.replace(' ', '').isalpha():
        print('Nome inválido! Digite apenas letras.')
        nome = input('Nome: ')

    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Idade inválida! Digite apenas números.')

    while True:
        telefone = input('Telefone: ')
        if telefone.isdigit():
            telefone = int(telefone)
            break
        else:
            print('Telefone inválido! Digite apenas números.')

    try:
        paciente = cadastrar(nome, idade, telefone)
        print(f'Paciente {paciente.nome} cadastrado com sucesso!')
    except ValueError as e:
        print(f'Erro ao cadastrar paciente: {e}')
        