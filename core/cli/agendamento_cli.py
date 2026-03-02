from workalendar.america import Brazil
cal = Brazil()
from datetime import date
from core.models.listas import pacientes
from core.services.agendamento import MESES
from core.services.agendamento import valida_data
from core.services.agendamento import agendar


def agendamento():
    print("\n=== Agendamento de Consultas ===")

    while True:
        mes = input('Qual o mês desejado para a consulta?\n'
                    'Mês: ')
        mes = MESES.get(mes)

        if mes is None:
            print("Opção inválida! Verifique se o mês foi digitado corretamente.")
            continue
        break
    while True:
        dia = input('Qual o dia desejado para a consulta?\n'
                    'Dia: \n')
        try:
            dia = int(dia)
            mes = int(mes)
        except ValueError:
            print("Opção inválida!")
            continue

        if valida_data(dia, mes, ano=2026)['data'] == True:
            print('Data aprovada!')
            
        while True:
            for index, paciente in enumerate(pacientes, 1):
                print(f'{index}. {paciente.nome}')
            paciente = input('Qual o nome do paciente que está agendando uma consulta?\n'
                            'Paciente: ').lower().strip()

            encontrados = [
            pac for pac in pacientes
            if paciente in pac.nome.lower()
            ]

            data = date(2026, mes, dia)

            if not encontrados:
                print("Não há nenhum paciente com esse nome.\n")
                continue
        
            elif len(encontrados) == 1:
                paciente = encontrados[0]
                if cal.is_working_day(data) == True:
                    agendar(paciente, 2026, mes, dia)
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
                                if cal.is_working_day(data) == True:
                                    agendar(paciente, 2026, mes, dia)
                                    print('Agendamento feito com sucesso.')
                                    break
                                else:
                                    print('Este dia não é dia útil.')
                                    continue
                            else:
                                print('Não foi possível encontrar esse paciente. Tente novamente mais tarde ou confira se ele foi cadastrado corretamente.')
                                continue
                    else:
                        print('Não foi possível encontrar esse paciente. Tente novamente mais tarde ou confira se ele foi cadastrado corretamente.')
                        continue
            else:
                print('Não foi possível encontrar esse paciente. Tente novamente mais tarde ou confira se ele foi cadastrado corretamente.')
                break