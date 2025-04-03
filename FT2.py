import pandas as pd
import matplotlib.pyplot as plt
import os

print("AULA 3 - Vizualizar dados")

path = r'C:\Users\HP\Desktop\Formação\Eisnt\UFCD 10809 - Visualização de dados em Python'
file = '02 uber_reviews_without_reviewid.csv'

__path__ = os.path.join(path, file)
file = pd.read_csv(__path__)

print(file.head()) # mostra primeiras 5 linhas
print(file.columns) # lista nome das colunas

print('\n2- Limpeza de dados')
file_clean = file.drop(columns=['userImage']) # Remove coluna userImage

print(file_clean.head()) # mostra primeiras 5 linhas da tabela limpa
print(file_clean.columns) # lista nome das colunas da tabela limpa

# Preenche valores nas colunas 'reviewCreatedVersion' e 'appVersion' com 'Teste'
file_clean.fillna({'reviewCreatedVersion': 'Teste'}, inplace=True)
file_clean.fillna({'appVersion': 'Teste'}, inplace=True)

print('\n3- Analise Descritiva')
print(file_clean['score'].value_counts().sort_index()) # mostra contagem de valores por avaliação (score)
print(file_clean['thumbsUpCount'].describe()) # resumo da distribuição de "thumbsUpCount" (gostos)


print('\n4- Distribuição temporal das análises')
file_clean['at'] = pd.to_datetime(file_clean['at'])  # Converter para datetime
file2=(file_clean['at'].dt.date.value_counts().sort_index().head()) # mostra os dados 5 primeiros dias
print(file2.sort_values()) # mostra a contagem de avaliações por data

print('\n5- Resumo de respostas')
print(file_clean[['replyContent', 'repliedAt']].dropna().head()) # mostra os dados 5 primeiros dias com resposta do Uber

print('\n6- Correlação entre score e thumbsUpCount')
print(file_clean[['score', 'thumbsUpCount']].corr()) # mostra a correlação entre score e thumbsUpCount

print('\n7- Visualização de insights adicionais')
print(file_clean['score'].value_counts().plot(kind='bar' , title='Contagens de Avaliações por score' )) # mostra a contagem de avaliações por score
plt.show() # mostra o gráfico   

print('\n8- Exportar dados limpos')
new_file='02 uber_reviews_without_reviewid_clean.csv'
file_clean.to_csv(os.path.join(path, new_file), index=False) # exporta o arquivo limpo

