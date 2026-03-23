from dados import cursor
accounts = {}

def carregar_usuarios():
    global accounts
    consulta = """SELECT usuário, senha FROM Usuarios;"""
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    accounts = {linha[0]: linha[1] for linha in linhas}

def valida(usuárioent, senhaent):
    global accounts
    carregar_usuarios()

    if usuárioent in accounts and accounts[usuárioent] == senhaent:
        return True
    else:
        return False