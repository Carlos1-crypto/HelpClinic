from dados import cursor
accounts = {}

def valida(usuárioent, senhaent):
    consulta = """SELECT * from usuários"""
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    for linha in linhas:
        accounts[linha[1]] = linha[2]
    if usuárioent in accounts and accounts[usuárioent] == senhaent:
        return True
    else:
        return False