from core.services.estatisticas import estatisticas

# Bloco de código para informar as estatísticas do sistema
def informações():

    dados = estatisticas()
    print('\n=== Informações do Sistema ===\n')
    
    print(f'A idade média dos pacientes é de {dados['media']:.2f} anos.'
        f"O sistema possui um total de {dados['pacientes']} pacientes.")

    if len(dados['lista_novos']) == 1:
        print(f'Dentre eles, o(a) paciente mais novo(a) é o(a) {dados['lista_novos'][0]} com {dados['mais_novo']} anos!')
    elif len(dados['lista_novos']) > 1:
        print(f'Dentre eles temos os nossos pacientes mais novos com {dados['mais_novo']} anos! Estes são:')
        for index, paciente in enumerate(dados['lista_novos'], start=1):
            print(f'{index}: {paciente}')

    if len(dados['lista_velhos']) == 1:
        print(f'Dentre eles, o(a) paciente mais velho(a) é o(a) {dados['lista_velhos'][0]} com {dados['mais_velho']} anos!')
    elif len(dados['lista_velhos']) > 1:
        print(f'Dentre eles temos os nossos pacientes mais velhos com {dados['mais_velho']} anos! Estes são:')
        for index, paciente in enumerate(dados['lista_velhos'], start=1):
            print(f'{index}: {paciente}')