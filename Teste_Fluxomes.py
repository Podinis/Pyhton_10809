import pyodbc
import pandas as pd
import matplotlib.pyplot as plt

# Configurações de conexão
config = {
    'driver': '{ODBC Driver 17 for SQL Server}',  # Certifique-se de que o driver está instalado
    'server': '128.0.0.82\sqlexpress',             # Substitua pelo seu servidor
    'database': 'fluxomesAcabamentos',              # Nome da base de dados
    'uid': 'sa',                                    # Substitua pelo seu usuário
    'pwd': 'Jpcamaju123!'                           # Substitua pela sua senha
}

try:
    # Estabelecendo a conexão
    connection_string = f"DRIVER={config['driver']};SERVER={config['server']};DATABASE={config['database']};UID={config['uid']};PWD={config['pwd']}"
    connection = pyodbc.connect(connection_string)

    print("Conexão bem-sucedida ao SQL Server")

    # Criando um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Executando o comando SELECT
    cursor.execute("SELECT * FROM dbo.OpOper WHERE dbo.OpOper.opId='929095'")

    # Recuperando todos os registros
    registros = cursor.fetchall()

    # Obtendo os nomes das colunas
    colunas = [column[0] for column in cursor.description]

    # Debug: Imprimindo o número de colunas e registros
    print(f"Número de colunas retornadas: {len(colunas)}")
    print(f"Número de registros retornados: {len(registros)}")

    # Verificando se há registros antes de criar o DataFrame
    if registros:
        # Convertendo os registros em um DataFrame do Pandas
        df = pd.DataFrame.from_records(registros, columns=colunas)
        df = df.dropna()

        # Agrupando e somando
        df_graf = df.groupby('OperationId')['Qty'].sum().reset_index()

        # Plotando o gráfico de barras
        plt.bar(df_graf['OperationId'], df_graf['Qty'])
        plt.xlabel('OperationId')
        plt.ylabel('Total Qty')
        plt.title('Total Quantity by OperationId')
        plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x, se necessário
        plt.tight_layout()  # Ajusta o layout para evitar sobreposição
        plt.show()

        # Definindo o caminho do arquivo de saída
        #output_file = r'C:\Users\podin\output2.xlsx'

        # Exportando o DataFrame para um arquivo Excel
        #df.to_excel(output_file, index=False)

        #print(f'== Dados exportados para {output_file} ==')
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