import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 7, 8, 6, 4]



fig, ax = plt.subplots(3, 3, figsize=(10, 10))

# Título da figura
fig.suptitle("Tipos de Graficos", fontsize=16, fontweight="bold");

# Subplot 1: Gráfico simples
ax[0, 0].plot(np.random.rand(10))
ax[0, 0].set_title("Gráfico Simples")

# Subplot 2: Gráfico com x e y
ax[0, 1].plot(x, y)
for i, j in zip(x, y):
    ax[0, 1].text(i, j, f'{j}', fontsize=8, fontweight="bold", color='blue' , ha='center', va='bottom')  # Adiciona os valores
ax[0, 1].set_title("Gráfico com x e y")

# Subplot 3: usando plt.subplots()
ax[0, 2].plot(np.random.rand(5), np.random.rand(5), color='red', marker='o', linestyle='--', linewidth=2, markersize=8)
ax[0, 2].set_title("Usando plt.subplots()")

# Subplot 4: usando plt.subplots() e desenhe x e x²
z= np.random.rand(10)
# Gráfico de dispersao
ax[1, 0].scatter(z, z**2, color='blue', marker='x', alpha=0.5)
ax[1, 0].set_title("desenhe x e x²")

# Subplot 5: exponencial (np.exp(X))
# Gráfico de linhas
ax[1, 1].plot(x, np.exp(x), color='blue', marker='x', alpha=0.5)
ax[1, 1].set_title("np.exp(X)")

# Subplot 6: dicionário Python de 3 produtos

prod = {'Product A': 150,
        'Product B': 200,
        'Product C': 300}
# Gráfico de barras
bars=ax[1, 2].bar(prod.keys(), prod.values(), color='purple', alpha=0.7, edgecolor='black')
for bar in bars:
    ax[1, 2].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height()}', ha='center', va='bottom', fontsize=8)  # Adiciona os valores
ax[1, 2].set_xlabel('Produtos')
ax[1, 2].set_ylabel('Valores')
ax[1, 2].set_title('Dicionário 3 produtos')


# Subplot 7: dicionário Python de 3 produtos horizontal
# Gráfico de barras horizontal 
ax[2, 0].barh(prod.keys(), prod.values(), color='purple', alpha=0.7, edgecolor='black')
ax[2, 0].set_xlabel('Produtos')
ax[2, 0].set_ylabel('Valores')
ax[2, 0].set_title('Dicionário 3 produtos horizontal')


# Subplot 8: dicionário Python de 3 produtos horizontal
# Gráfico de dispersão  
scatter = ax[2, 1].scatter(prod.keys(), prod.values(), color='purple', alpha=0.7, edgecolor='black')
ax[2, 1].legend(*scatter.legend_elements(), loc="center right", title="Produtos")
ax[2, 1].set_title('Scatter Produtos')

# Subplot 9: 1000 números aleatórios
x=np.random.rand(1000)
# Gráfico de histograma
ax[2, 2].hist(x, bins=30, color='purple', alpha=0.7, edgecolor='black')
ax[2, 2].set_title('Histograma 1000 núm. aleatórios')

plt.tight_layout()
plt.show()

