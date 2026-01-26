from core.models.listas import pacientes

# Bloco de código para informar as estatísticas do sistema
def estatisticas():
    print('\n=== Informações do Sistema ===\n')
    # Checagem de pacientes, se não o sistema avisa e retorna para o bloco inicial
    if not pacientes:
        print('Nenhum cliente cadastrado.')
        return
    # Bloco de código que faz o cálculo de todas as idades dos pacientes e divide pelo número de pacientes, criando a média das idades
    total_anos = 0
    for paciente in pacientes:
        total_anos += paciente.idade
    media = total_anos / len(pacientes)
    print(f'A idade média dos pacientes é de {media} anos.'
        f"O sistema possui um total de {len(pacientes)} pacientes.")

    # Bloco de código que checa a idade de todos os pacientes e armazena a menor delas na variável mais_novo, depois checa se há mais alguém com essa mesma idade,
    # se sim, o sistema coloca todos os pacientes que tem a idade igual a menor idade, inclusive a menor idade, em uma lista chamada pac_mais_novos, logo após cria
    # uma frase para ser exibida se apenas um paciente tiver a menor idade, e outra frase se houver mais idades iguais a essa seguida de um for para listar todos
    # os pacientes que possuem essa idade. E assim se segue com os pacientes mais velhos
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