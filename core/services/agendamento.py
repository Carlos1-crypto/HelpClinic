from core.models.listas import agendamentos
from core.models.Classes import Consulta
from workalendar.america import Brazil
cal = Brazil()
import datetime

MESES = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12
    }

def valida_data(dia: int, mes: int, ano: int):
    try:
        data = datetime.date(year=ano, month=mes, day=dia)
    except ValueError:
        raise ValueError("Data inválida.")
    
    return {
        'data': data,
        'dia': dia,
        'mes': mes,
        'ano': ano
            }
    
def agendar(paciente: str, ano: int, mes: int, dia: int):
    try:
        data = datetime.date(ano, mes, dia)
    except ValueError:
        raise ValueError('Data inválida')
    try:
        agendamentos.append(Consulta(paciente.nome, paciente.telefone, data))
    except ValueError:
        raise ValueError('Algo deu errado.')