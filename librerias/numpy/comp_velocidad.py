import numpy as np
import time

SIZE = 1_000_000

# Listas (analisis con Python)
L1 = range(SIZE)
L2 = range(SIZE)
# Arrays = Vectores (analisis con NumPy)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

# Analisis rapi
start = time.time()  # el metodo time() de la clase tiempo me da el tiempo UNIX (segundos transcurridos desde 1/01/1970 00:00)
result = [(x, y) for x, y in zip(L1, L2)]  # Calculo la suma de las 2 listas
print("Resultado lista de Python: ")
print((time.time() - start) * 1000)  # Con esta resta puedo saber el tiempo exacto que tardo desde start a este momento (x 1000 p/mseg) 
print("------------------------------")
start = time.time()
result = A1 + A2
print("Resultado NumPy array:")
print((time.time() - start) * 1000)

