import numpy as np

a = np.array([(1,2,3)])
print("1D array: ")
print(a)
print("------------------------------")
b = np.array([(1,2,3),(4,5,6)])
print("2D array: ")
print(b)
print("------------------------------")

# ---------- Matrices ----------
print("---------- Matrices ----------")

# Crear matriz de unos - 3 filas 4 columnas
unos = np.ones((3,4)) 
print(unos)
print("------------------------------")

# Crear matriz de ceros - 3 filas 4 columnas
ceros = np.zeros((3,4))
print(ceros)
print("------------------------------")

# Crear matriz con valores aleatorios
aleatorios = np.random.random((2,2))
print(aleatorios)
print("------------------------------")

# Crear matriz vacia
vacia = np.empty((3,2))
print(vacia)
print("------------------------------")

# Crear matriz con un solo valor
full = np.full((2,2), 8)
print(full)
print("------------------------------")

# Crear matriz con valores espaciados uniformemente
espacio1 = np.arange(0, 30, 5)  # matriz 1D con valores de 0 a 30 de 5 en 5
print(espacio1)

espacio2 = np.linspace(0,2, 5)  # matriz 1D con valores de 0 a 2 de 0.5 en 0.5
print(espacio2)
print("------------------------------")

# Crear matriz identidad
identidad1 = np.eye(4,4)
print(identidad1)

identidad2 = np.identity(4)
print(identidad2)

# ---------- Inspeccionar matrices ----------
print("---------- Inspeccionar matrices ----------")

# Conocer las dimensiones de una matriz
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print("------------------------------")

# Conocer el tipo de los datos
print(a.dtype)
print("------------------------------")

# Conocer el tamaño y forma de la matriz
a = np.array([(1,2,3,4,5,6)])
print(a.size)  # tamaño
print(a.shape)  # forma
print("------------------------------")

# ---------- Cambio de tamaño y forma de las matrices ----------
print("---------- Cambio de tamaño y forma de las matrices ----------")
a = np.array([(8,9,10),(11,12,13)])
print(a)  # Forma 1
a = a.reshape(3,2)  # Forma 2
print(a)
print("----------------------------")
# Extraer un solo valor de la matriz - el valor ubicado en la fila 0 columna 2
a = np.array([(1,2,3,4),(5,6,7,8)])
print(a[0,2])
print("----------------------------")

# ---------- Operaciones matematicas con NumPy ----------
print("---------- Operaciones matematicas con NumPy ----------")

# Encontrar el minimo, maximo y la suma
a = np.array([2,4,8])
print(a.min())
print(a.max())
print(a.sum())
print("----------------------------")

# Calcular la raiz cuadrada y la desviacion estandar de la matriz
a = np.array([(1,2,3,4),(5,6,7,8)])
print(np.sqrt(a))  # Raiz cuadrada
print(np.std(a)) # Desviacion estandar de la matriz
print("----------------------------")

# Calcular la suma, resta, multiplicacion y division de dos matrices
x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])
print(x + y)
print(x - y)
print(x * y)
print(x / y)