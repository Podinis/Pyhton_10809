import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# Configurações de conexão
config = {
    'driver': '{Progress OpenEdge 11.6 Driver}',  # Certifique-se de que o driver está instalado
    'server': '128.0.150.57',                     # Substitua pelo seu servidor
    'port'  : '44000' ,                           # Porta seu servidor
    'database': 'spnoba',                         # Nome da base de dados
    'uid': 'root',                                # Substitua pelo seu usuário
    'pwd': 'cognos'                               # Substitua pela sua senha
}

try:
    # Estabelecendo a conexão
    connection_string = f"DRIVER={config['driver']};SERVER={config['server']};PORT={config['port']};DATABASE={config['database']};UID={config['uid']};PWD={config['pwd']}"
    connection = pyodbc.connect(connection_string)

    print("Conexão bem-sucedida ao SQL Server")

    # Criando um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Executando o comando SELECT
    cursor.execute("SELECT *  FROM cocent where cocent.datemicent >'01/01/2025'")

    # Recuperando todos os registros
    registros = cursor.fetchall()

    # Obtendo os nomes das colunas
    colunas = [column[0] for column in cursor.description]

    # Verificando se há registros antes de criar o DataFrame
    if registros:
        print("Registro encontrado.")
    else:
        print("Nenhum registro encontrado.")

except pyodbc.Error as err:
    print(f"Erro: {err}")

finally:
    # Fechando a conexão
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("Conexão ao SQL Server fechada")