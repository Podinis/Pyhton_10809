import matplotlib.pyplot as plt
import numpy as np


# 2. Crie um plot simples usando plt.plot()
plt.plot()
plt.title("2 - Plot simples")
plt.show()


# 3. Desenhe um gráfico com uma única lista Python
plt.plot(np.random.rand(10))
plt.title("3 - Gráfico Simples")
plt.show()


#4. Crie duas listas, uma chamada x, outra chamada y cada uma com 5 números. Desenhe um gráfico com as duas listas.
x = [1, 2, 3, 4, 5]
y = [10, 7, 8, 6, 4]
plt.plot(x)
plt.plot(y)
# for i, j in zip(x, y):
#     ax[0, 1].text(i, j, f'{j}', fontsize=8, fontweight="bold", color='blue' , ha='center', va='bottom')  # Adiciona os valores
plt.title("4 - Gráfico com 2 Listas")

#5. Crie um gráfico usando pls.subplots()
fig, ax = plt.subplots(3, 3, figsize=(10, 10))
# Título da figura
fig.suptitle("Tipos de Graficos", fontsize=16, fontweight="bold");

# Subplot 1: Crie um gráfico usando pls.subplots()
ax[0, 0].plot( )
ax[0, 0].set_title("5 - Usando plt.subplots()")

#6. Crie um plot usando plt.subplots() e adicione as listas x & y
# Subplot 2
ax[0, 1].set_title("6 - Usando subplots listas x & y")
ax[0, 1].plot(x, y, color='blue', marker='o', alpha=0.5)


#8. Crie um array de 100 números (distribuídos normalmente) entre 0 e 100 e guarde o array numa variável x
z= np.linspace(0, 100, 100)


#9. Crie um plot usando plt.subplots() e desenhe x e x²
# Subplot 3: usando plt.subplots() e desenhe x e x²
# Gráfico de dispersao
ax[0, 2].plot(z, z**2, label="x²", color='blue', marker='x', alpha=0.5)
ax[0, 2].set_title("9 - desenhe x e x²")


#10. Crie uma gráfico de dispersão de X e X exponencial (np.exp(X))
# Subplot 4: exponencial (np.exp(X))
# Gráfico de linhas
y = [1, 2, 3, 4, 5]
ax[1, 0].scatter(y, np.exp(y), color='blue', marker='x', alpha=0.5, label="np.exp(x)")
ax[1, 0].set_title("np.exp(X)")


#11. Crie um dicionário Python de 3 produtos. As chaves do dicionário podem ser nomes de alimentos e os valores podem ser preços
prod = {'Product A': 150,
        'Product B': 200,
        'Product C': 300}


#12. Crie um gráfio de barras onde x-axis recebe como valor as chaves do dicionárioe y-axis recebe os valores do dicionário
# Subplot 5: dicionário Python de 3 produtos
# Gráfico de barras
bars=ax[1, 1].bar(prod.keys(), prod.values(), color='purple', alpha=0.7, edgecolor='black')
for bar in bars:
    ax[1, 1].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height()}', ha='center', va='bottom', fontsize=8)  # Adiciona os valores
ax[1, 1].set_title('Dicionário 3 produtos')    


#13. Adicione um título, xlabel e ylabel ao último plot criado
ax[1, 1].set_xlabel('Produtos')
ax[1, 1].set_ylabel('Valores')


#14. Faça o mesmo plot, dessa vez com barras horizontais
# Subplot 6: dicionário Python de 3 produtos horizontal
# Gráfico de barras horizontal 
ax[1, 2].barh(prod.keys(), prod.values(), color='purple', alpha=0.7, edgecolor='black')
ax[1, 2].set_xlabel('Produtos')
ax[1, 2].set_ylabel('Valores')
ax[1, 2].set_title('Dicionário 3 produtos horizontal')


# Subplot 7: 
# Gráfico de dispersão  
scatter = ax[2, 0].scatter(prod.keys(), prod.values(), color='purple', alpha=0.7, edgecolor='black')
ax[2, 0].legend(*scatter.legend_elements(), loc="center right", title="Produtos")
ax[2, 0].set_title('Scatter Produtos')


#15. Crie um array de 1000 números aleatórios distribuídos normalmente e desenhe um histograma com o mesmo.
# Subplot 8: 1000 números aleatórios
x=np.random.rand(1000)
# Gráfico de histograma
ax[2, 1].hist(x, bins=30, color='purple', alpha=0.7, edgecolor='black')
ax[2, 1].set_title('Histograma 1000 núm. aleatórios')

# Subplot 9: 

foodPreferance = ['Vegetarian', 'Non Vegetarian','Vegan', 'Eggitarian']  
consumers = [30,100,10,60]  

ax[2,2].axis('equal')
ax[2, 2].pie(consumers, labels = foodPreferance, autopct='%1.2f%%')
ax[2, 2].set_title('Preferência Alimentar')
#ax[2, 2].set_visible(False)  # Oculta o último subplot

plt.tight_layout()
plt.show()

