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
    cursor.execute("SELECT  dbo.tbEncomenda.NumEnc, dbo.tbEncomenda.NumExtEnc, dbo.tbEncomenda.numter, dbo.tbEncomenda.desNumter, dbo.tbEncomenda.data, dbo.tbEncomenda.refcom, dbo.tbEncomenda.dataPedido, dbo.tbEncomenda.datacriacao, dbo.tbLinhaEnc.descricao, dbo.tbLinhaEnc.qty, dbo.tbLinhaEnc.seqNumEnc FROM dbo.tbEncomenda INNER JOIN dbo.tbLinhaEnc ON dbo.tbEncomenda.NumEnc = dbo.tbLinhaEnc.NumEnc where dbo.tbEncomenda.estado<>'S' and dbo.tbLinhaEnc.estado<>'S' and dbo.tbEncomenda.data >'01/01/2025'")

    # Recuperando todos os registros
    registros = cursor.fetchall()

    # Obtendo os nomes das colunas
    colunas = [column[0] for column in cursor.description]

    # Verificando se há registros antes de criar o DataFrame
    if registros:
        # Convertendo os registros em um DataFrame do Pandas
        df = pd.DataFrame.from_records(registros, columns=colunas)
        df['qty'] = pd.to_numeric(df['qty'], errors='coerce')

        df.columns = df.columns.str.strip()
        
        # print("Colunas do DataFrame:", df.columns)  # Verificando as colunas
        #print("Primeiras linhas do DataFrame:\n", df.head())  # Verificando os dados
       
        df = df.dropna(subset=['NumEnc', 'numter'])  # Removendo apenas linhas com nulos nessas colunas
        #print("Primeiras linhas do DataFrame:\n", df.head())
       # Agrupando e somando
        try:
            df_graf = df.groupby('numter')['qty'].sum().reset_index()
            print("\nDataFrame agrupado:")
            print(df_graf)
        except KeyError as e:
            print(f"KeyError: {e}. Verifique se a coluna existe.")
                
        media_enc = df.groupby('numter')['qty'].mean()
        # Plotando o gráfico de barras
        fig, ax1 = plt.subplots(figsize=(8, 5))
        ax1.bar(df_graf['numter'],df_graf['qty'],label="df_graf['numter']" ,)
        ax1.set_xlabel('operationId')
        ax1.set_ylabel('Total Qty')
        ax1.set_xticks(range(len(df_graf.numter)), labels=df_graf.numter,rotation=45, ha="right", rotation_mode="anchor")
        ax1.set_title('Total Quantity by Operation')
        
        ax2=ax1.twinx()
        ax2.plot(df_graf['numter'],media_enc,color='red', marker='o', label='Média')
        plt.tight_layout()  # Ajusta o layout para evitar sobreposição
        plt.grid(True, linestyle='--')
        plt.show()

        contagem = df["numter"].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(contagem.values, autopct='%1.1f%%', startangle=140)
        plt.title("Distribuição de Encomendas no Dataset")
        plt.legend(title="Clientes", labels=contagem.index, loc="upper right")
        plt.show()

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