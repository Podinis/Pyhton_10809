import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Criar um DataFrame com uma coluna de comentários (simulado)
df = pd.DataFrame({
    'comentarios': [
        'A plataforma é intuitiva e rápida.',
        'Excelente apoio ao cliente e suporte técnico.',
        'Muito eficaz e bem estruturado.',
        'Gostei da experiência de utilização.',
        'Sistema leve e fácil de navegar.'
    ]
})

# Concatenar todos os comentários numa única string separada por espaços
texto = ' '.join(df['comentarios'])

# Criar um conjunto de palavras a ignorar (stopwords)
stopwords = set(STOPWORDS)
# Acrescentar algumas palavras irrelevantes específicas para português
stopwords.update(['de', 'e', 'da', 'ao'])

# Criar o objeto WordCloud com parâmetros personalizados
wordcloud = WordCloud(
    width=800,                # Largura da imagem
    height=400,               # Altura da imagem
    background_color='white', # Cor de fundo
    colormap='viridis',       # Paleta de cores
    stopwords=stopwords,      # Palavras a ignorar
    max_words=50              # Máximo de palavras visíveis
).generate(texto)             # Gerar a nuvem a partir do texto

# Mostrar a imagem gerada
plt.figure(figsize=(10, 5))        # Definir o tamanho da figura
plt.imshow(wordcloud, interpolation='bilinear')  # Desenhar a nuvem
plt.axis('off')                    # Retirar eixos
plt.title('Nuvem de Palavras - Comentários dos Utilizadores')  # Título
plt.show()                         # Apresentar o gráfico
