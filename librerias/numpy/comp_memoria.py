import numpy as np
import sys  # Modulo sys proporciona acceso a algunas variables utilizadas por el interprete

# Comparamos la memoria que ocupa una lista de Python versus un array con NumPy (de 1000 numero ambas)
S = range(1000)  # Generamos una lista de 1000 numeros
print("Resultado lista de Python:")
print(sys.getsizeof(5)*len(S))  # Calculo de la memoria asiganada a los 1000 numeros
print("------------------------------")
D = np.arange(1000)  # Generamos un array de 1000 numeros
print("Resultado NumPy array: ")
print(D.size * D.itemsize)  # Calculo de la memoria asiganada al array

# 28_000/8_000 = 3.5 
# 3.5 veces mas rapido es calcular sumas de array con NumPy que calcular la suma de listas con Python

