# Arquivo principal para executar o servidor Flask

import sys
from app import app  # Importar app do arquivo centralizado
import routes  # Registrar routes (evita importação circular)

def run_server():
    app.run(debug=True)

def main():
    # Execute o servidor Flask por padrão.
    run_server()

if __name__ == '__main__':
    main()