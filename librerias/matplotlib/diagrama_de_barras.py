import matplotlib.pyplot as plt

# Definir los datos
x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
y1 = [10, 55, 88, 32, 40]
x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
y2 = [42, 26, 10, 29, 66]

# Configurar las características del gráfico
plt.bar(x1, y1, label='Datos 1', width=0.5, color='lightblue')
plt.bar(x2, y2, label='Datos 2', width=0.5, color='orange')

# Definir título y nombres de ejes
plt.title('Gráfico de barras')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda, grilla en 'y' y figura
plt.legend()
plt.grid(axis='y')
plt.show()
