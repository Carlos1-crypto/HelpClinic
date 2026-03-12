from core.cli.cadastro_cli import cadastro
from core.cli.estatísticas_cli import informações
from core.cli.busca_cli import busca
from core.cli.lista_cli import lista
from core.cli.corrigir_cli import corrigir
from core.cli.agendamento_cli import agendamento
from core.cli.checarconsultas_cli import consultas
import sys
from flask import Flask


app = Flask(__name__)

from routes import *

def run_server():
    app.run(debug=True)




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
                informações()
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


def main():
    # Execute o servidor Flask por padrão. Use --cli para rodar a versão de terminal.
    if "--cli" in sys.argv:
        recepcao()
    else:
        run_server()


if __name__ == '__main__':
    main()