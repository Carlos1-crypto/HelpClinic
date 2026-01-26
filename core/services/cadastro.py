from core.models.Classes import Paciente
from core.models.listas import pacientes

# Bloco de código para o cadastro de novos pacientes e suas informações
def cadastro():
    print("\n=== Cadastro de Paciente ===")
    nome = input("Nome: ")
    # While para checar se todos os digitos do nome do paciente realmente são letras
    while not nome.replace(' ', '').isalpha():
        print('Nome inválido! Digite apenas letras.')
        nome = input("Nome: ")
    # While true com break para que o sistema só pare de pedir a idade e o telefone quando o tipo da inforamção forem números inteiros
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

    # Atribuição do novo paciente com a classe Paciente que possui nome, idade e telefone, e adicionando a lista pacientes
    novo = Paciente(nome, idade, telefone)
    pacientes.append(novo)
    print(f"Paciente {nome} cadastrado com sucesso!")