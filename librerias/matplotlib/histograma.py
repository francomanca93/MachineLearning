import matplotlib.pyplot as plt

# Histogramas
# Se usan para mostrar una distribucion.
# Son utilies cuando tenes una lista muy larga o matrices.

# Definir los datos
a = [22, 55, 62, 45, 21, 22, 34, 42, 4, 2, 102, 95, 85, 55, 110, 120, 70, 65, 55, 111, 115, 80, 75, 65, 54, 44, 43, 42, 48]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # Compartimentos donde estarán ubicados los datos 'a'

# Configurar las características del gráfico
plt.hist(a, bins, histtype='bar', rwidth=0.8, color='lightgreen')

# Definir título y nombres de ejes
plt.title('Histogramas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar filas
plt.show()