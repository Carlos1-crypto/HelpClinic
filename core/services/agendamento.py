from core.models.listas import pacientes
from workalendar.america import Brazil
cal = Brazil()
import datetime

def agendamento():
    print("\n=== Agendamento de Consultas ===")
    ano = 2026

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

    while True:
        mes = input('Qual o mês desejado para a consulta?\n'
                    'Mês: ')
        mes = MESES.get(mes)

        if mes is None:
            print("Opção inválida!")
            continue
        dia = input('Qual o dia desejado para a consulta?\n'
                    'Dia: ')
        try:
            dia = int(dia)
            mes = int(mes)
            ano = int(ano)
        except ValueError:
            print("Opção inválida!")
            continue

        try:
           data = datetime.date(year=ano, month=mes, day=dia)
        except ValueError:
            print("Data inválida.")
            continue
        
        num = 1
        print()
        for p in pacientes:
            print(f'{num}. {p.nome}')
            num = num + 1
        print()
            
        while True:
            paciente = input('Qual o nome do paciente que está agendando uma consulta?\n'
                            'Paciente: ').lower().strip()
            encontrados = [
                pac for pac in pacientes
                if paciente in pac.nome.lower()
                ]

            if not encontrados:
                print("Não há nenhum paciente com esse nome.")
                print()
                continue
            
            elif len(encontrados) == 1:
                paciente = encontrados[0]
                if cal.is_working_day(data):
                    paciente.agendar(data)
                    print('Agendamento feito com sucesso.')
                    return
                else:
                    print('Este dia não é dia útil.')
                    break
            elif len(encontrados) > 1:
                print("Mais de um paciente encontrado:")
                for i, pac in enumerate(encontrados, 1):
                    print(f"{i}. {pac.nome}")
                while True:
                    resp = input('\nQual deles é o que você está procurando?'
                                 'Resposta: ').lower().strip()
                    if resp in encontrados:
                        for i in encontrados:
                            if i in resp:
                                if cal.is_working_day(data):
                                    paciente.agendar(data)
                                    print('Agendamento feito com sucesso.')
                                    break
                                else:
                                    print('Este dia não é dia útil.')
                                    continue
                            else:
                                print('Não foi possível encontrar esse paciente. Tente novamente mais tarde ou confira se ele foi cadastrado corretamente.')
                                break
                    else:
                        print('Não foi possível encontrar esse paciente. Tente novamente mais tarde ou confira se ele foi cadastrado corretamente.')
                        break
            else:
                print('Não foi possível encontrar esse paciente. Tente novamente mais tarde ou confira se ele foi cadastrado corretamente.')
                break
            