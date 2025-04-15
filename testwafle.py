import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle

# 1. Criar um DataFrame com os dados
df = pd.DataFrame({
    'Animal': ['Cão', 'Gato'],
    'Qtd': [50, 30]
})

# 2. Converter o DataFrame num dicionário: {'Cão': 50, 'Gato': 30}
data_dict = dict(zip(df['Animal'], df['Qtd']))

# 3. Criar o gráfico Waffle com matplotlib + Waffle
fig = plt.figure(
    FigureClass=Waffle,  # Indica que esta figura é do tipo Waffle
    rows=5,              # Número de linhas da grelha
    values=data_dict,    # Dicionário de categorias e valores
    title={'label': 'Distribuição de Animais', 'loc': 'left'},  # Título do gráfico
    labels=[f"{k} ({v})" for k, v in data_dict.items()],        # Rótulos com nome e valor
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}      # Posição da legenda
)

# 4. Mostrar o gráfico
plt.show()