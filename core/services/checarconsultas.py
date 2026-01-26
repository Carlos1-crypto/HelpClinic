from core.models.listas import agendamentos

def consultas():
    if agendamentos:
        for consulta in agendamentos:
            print(f'Paciente: {consulta.nome} | Data: {consulta.data}')
    else:
        print('Não há agendamentos feitos.')