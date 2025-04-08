import matplotlib.pyplot as plt 
# Definir vetores
x = [10, 20, 30, 40] 
y = [20, 30, 40, 50] 
# criar grafico
plt.plot(x, y) 
# Adicionar titulo 
plt.title("Grafico Simples") 
# Adding the labels 
plt.ylabel("y-axis") 
plt.xlabel("x-axis") 
#Mostrar o grafico
plt.show() 

plt.scatter(x, y)   
plt.title("Grafico Dispersão") 
plt.show() 

plt.bar(x, y)   
plt.title("Grafico Barras") 
plt.show() 

plt.barh(x, y)   
plt.title("Grafico Barras Horizontal") 
plt.grid()
plt.show() 

plt.hist(x, bins=10, color='purple', alpha=0.7, edgecolor='black')   
plt.hist(y, bins=10, color='blue', alpha=0.7, edgecolor='black')   
plt.title("Grafico Histograma") 
plt.show() 

plt.pie(x, labels=x, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Grafico Pizza")
plt.legend(['Teste Legenda'], loc ="lower left")
plt.show()

plt.boxplot(x)
plt.title("Grafico Boxplot")
plt.show()

plt.violinplot(x)
plt.title("Grafico Violinplot")
plt.show()

plt.polar(x, y)
plt.title("Grafico Polar")
plt.show()	