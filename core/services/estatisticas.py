from core.models.listas import pacientes

def estatisticas():
    # Checagem de pacientes, se não o sistema avisa e retorna para o bloco inicial
    if not pacientes:
        raise ValueError('Não há pacientes cadastrados')
    
    # Bloco de código que faz o cálculo de todas as idades dos pacientes e divide pelo número de pacientes, criando a média das idades
    total_anos = 0
    for paciente in pacientes:
        total_anos += paciente.idade
    media = total_anos / len(pacientes)

    total_pacientes = len(pacientes)
    
    # Bloco de código que checa a idade de todos os pacientes e armazena a menor delas na variável mais_novo, depois checa se há mais alguém com essa mesma idade,
    # se sim, o sistema coloca todos os pacientes que tem a idade igual a menor idade, inclusive a menor idade, em uma lista chamada pac_mais_novos, logo após cria
    # uma frase para ser exibida se apenas um paciente tiver a menor idade, e outra frase se houver mais idades iguais a essa seguida de um for para listar todos
    # os pacientes que possuem essa idade. E assim se segue com os pacientes mais velhos
    # Opção 1: Trabalhar apenas com nomes (recomendado)

    # Encontrar a idade mínima e máxima
    mais_novo = min(p.idade for p in pacientes)
    mais_velho = max(p.idade for p in pacientes)

    # Listas apenas com nomes
    pac_mais_novos = [p.nome for p in pacientes if p.idade == mais_novo]
    pac_mais_velhos = [p.nome for p in pacientes if p.idade == mais_velho]

    # Remover duplicatas (se houver)
    lista_novos = list(set(pac_mais_novos))
    lista_velhos = list(set(pac_mais_velhos))

    return {
        'media': media,
        'pacientes': total_pacientes,
        'lista_novos': lista_novos,
        'lista_velhos': lista_velhos,
        'mais_novo': mais_novo,
        'mais_velho': mais_velho,
        }