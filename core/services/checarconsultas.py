<<<<<<< HEAD
from core.models.listas import agendamentos

def consultas():
    if agendamentos:
        for consulta in agendamentos:
            print(f'Paciente: {consulta.nome} | Data: {consulta.data}')
    else:
=======
from core.models.listas import agendamentos

def consultas():
    if agendamentos:
        for consulta in agendamentos:
            print(f'Paciente: {consulta.nome} | Data: {consulta.data}')
    else:
>>>>>>> 68d5e56a6b2bddfafb336fdda378298995c3ceab
        print('Não há agendamentos feitos.')