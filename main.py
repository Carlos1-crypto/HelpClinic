import time
import sys


class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone


pacientes = []


def cadastro():
    print("\n=== Cadastro de Paciente ===")
    nome = input("Nome: ")
    while not nome.replace(' ', '').isalpha():
        print('Nome inválido! Digite apenas letras.')
        nome = input("Nome: ")

    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Idade inválida! Digite apenas números.")

    while True:
        telefone = input("Telefone: ")
        if telefone.isdigit():
            telefone = int(telefone)
            break
        else:
            print("Telefone inválido! Digite apenas números.")

    novo = Paciente(nome, idade, telefone)
    pacientes.append(novo)
    print(f"Paciente {nome} cadastrado com sucesso!")


def recepcao():
    print("Seja bem vindo ao HelpClinic!")

    while True:
        resp = input(
            "\nO que deseja fazer?\n"
            "1. Cadastrar paciente\n"
            "2. Ver estatísticas\n"
            "3. Buscar paciente\n"
            "4. Listar todos os pacientes\n"
            "5. Sair\n"
            "Escolha uma opção: "
        )
        pontos = ''
        msg = 'Carregando'
        for i in range(3):
            pontos = pontos + '.'
            print(msg + pontos)
            time.sleep(0.5)

        match resp:
            case '1':
                cadastro()

            case '2':
                print('\n=== Informações do Sistema ===\n')

                if not pacientes:
                    print('Nenhum cliente cadastrado.')
                    continue

                total_anos = 0
                for paciente in pacientes:
                    total_anos += paciente.idade
                media = total_anos / len(pacientes)
                print(f'A idade média dos pacientes é de {media} anos.')

                print(f"O sistema possui um total de {len(pacientes)} pacientes.")

                mais_novo = pacientes[0]
                pac_mais_novos = []
                for pac in pacientes:
                    if pac.idade < mais_novo.idade:
                        mais_novo = pac
                for pac in pacientes:
                    if pac.idade == mais_novo.idade:
                        pac_mais_novos.append(pac)
                if len(pac_mais_novos) == 1:
                    print(f'Dentre eles, o(a) paciente mais novo(a) é o(a) {mais_novo.nome} com {mais_novo.idade} anos!')
                elif len(pac_mais_novos) > 1:
                    print(f'Dentre eles temos os nossos pacientes mais novos com {mais_novo.idade} anos! Estes são:')
                    num = 1
                    for pac in pac_mais_novos:
                        print(f'{num}. {pac.nome}')
                        num = num + 1

                mais_velho = pacientes[0]
                pac_mais_velhos = []
                for pac in pacientes:
                    if pac.idade > mais_velho.idade:
                        mais_velho = pac
                for pac in pacientes:
                    if pac.idade == mais_velho.idade:
                        pac_mais_velhos.append(pac)
                if len(pac_mais_velhos) == 1:
                    print(f'Dentre eles, o(a) paciente mais velho(a) é o {mais_velho.nome} com {mais_velho.idade} anos!')
                elif len(pac_mais_velhos) > 1:
                    print(f'Dentre eles temos os nossos pacientes mais velhos com {mais_velho.idade} anos! Estes são:')
                    num = 1
                    for pac in pac_mais_velhos:
                        print(f'{num}. {pac.nome}')
                        num = num + 1

            case '3':
                print('\n=== Busca de Paciente ===\n')
                procura = input('Qual é o nome do paciente que está procurando?\n'
                                'Paciente: ')
                encontrado = None

                for paciente in pacientes:
                    if procura.lower() in paciente.nome.lower():
                        encontrado = paciente
                if encontrado:
                    print('\nAqui estão as informações do paciente:\n'
                          f'Nome: {encontrado.nome}\n'
                          f'Idade: {encontrado.idade}\n'
                          f'Telefone: {encontrado.telefone}\n')
                else:
                    print(
                        '\nPaciente não encontrado, verifique se o nome foi escrito corretamente ou cadastre o paciente primeiro.\n')

            case '4':
                print('\n=== Lista de Pacientes ===\n')
                num = 1
                for paciente in pacientes:
                    print(f'{num}. {paciente.nome}')
                    num = num + 1

            case '5':
                print('Saindo...')
                break

            case _:
                print("Opção inválida!")

recepcao()
