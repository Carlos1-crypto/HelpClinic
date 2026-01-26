from core.services.cadastro import cadastro
from core.services.estatisticas import estatisticas
from core.services.busca import busca
from core.services.lista import lista
from core.services.corrigir import corrigir
from core.services.agendamento import agendamento
from core.services.checarconsultas import consultas

# Primeiro bloco do código que o sistema executa que leva para as outras funções do sistema
def recepcao():
    print("Seja bem vindo ao HelpClinic!")
    # While true para que o programa não termine a menos que o usuário queira
    while True:
        resp = input(
            "\nO que deseja fazer?\n"
            "1. Cadastrar paciente\n"
            "2. Ver estatísticas\n"
            "3. Buscar paciente\n"
            "4. Listar todos os pacientes\n"
            "5. Corrigir um cadastro\n"
            "6. Agendar uma consulta\n"
            "7. Ver as consultas\n"
            "8. Sair\n"
            "Escolha uma opção por número: "
        )

        # Direcionador correspondente a resposta do usuário
        match resp:
            case '1':
                cadastro()
            case '2':
                estatisticas()
            case '3':
                busca()
            case '4':
                lista() 
            case '5':
                corrigir()
            case '6':
                agendamento()
            case '7':
                consultas()
            case '8':
                print('Saindo...')
                break
            case _:
                print("Opção inválida!")

recepcao()
