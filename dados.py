import pyodbc

dados_conexao = (
    "Driver={MySQL ODBC 9.6 Unicode Driver};"
    "Server=DSBWS009;"
    "Database=db_helpclinic;"
    "User=root;"
    "Password=198119;"
    "Port=;"
    "Port=;"
)

try:
    conexao = pyodbc.connect(dados_conexao)
    print('Conexão bem sucedida.')
except ValueError:
    raise ValueError('A conexão não deu certo.')

cursor = conexao.cursor()