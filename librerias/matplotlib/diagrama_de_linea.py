import matplotlib.pyplot as plt

# Definir los datos
x1 = [3, 4, 5, 6]
y1 = [5, 6, 3, 4]
x2 = [2, 5, 8]
y2 = [3, 4, 3]

# Configurar las caracteristicas del gráfico
plt.plot(x1, y1, label= 'Linea 1', linewidth=2, color='blue')
plt.plot(x2, y2, label= 'Linea 2', linewidth=2, color='green')

# Definir título y nombres de ejes
plt.title('Diagrama de líneas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda, cuadrícula y figura
plt.legend()
plt.grid(True)
plt.show()