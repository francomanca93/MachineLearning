# Funciones para explorar y trabajar con un Data Frame
# importo librerias
import numpy as np
import pandas as pd

# Creo data frame simple
df = pd.DataFrame(np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
print("DataFrame: ")
print(df)

print("\n-------------- Juguemos con el Data Frame ----------------\n")

# Forma del DataFrame
print("Forma del DataFrame: ")
print(df.shape)
print("----------------------------")

# Altura del DataFrame
print("Altura del DataFrame: ")
print(len(df.index))
print("----------------------------")

print(" \n ---------------- Seleccion de datos ----------------\n")

# Seleccionar la primer columna del DataFrame
print("Primer columna del DataFrame")
print(df[0])
print("----------------------------")

# Seleccionar dos columnas del DataFrame
print("Dos columnas del DataFrame")
print(df[[0, 1]])
print("----------------------------")

# Seleccionar el valor de la primera fila y la última columna del DataFrame
print("Valor de la primera fila y la última columna del DataFrame")
print(df.iloc[0][2])
print("----------------------------")

# Seleccionar los valores de la primera fila del DataFrame
print("Valor de la primera fila del DataFrame")
print(df.loc[0])  # Tambien con df.iloc[0,:]
print("----------------------------")

print(" \n ---------------- Estadísticas ----------------\n")
# Estadísticas del DataFrame
print("Estadísticas del DataFrame: ")
print(df.describe())
print("----------------------------")

# Media de las columnas DataFrame
print("Media de las columnas DataFrame: ")
print(df.mean())
print("----------------------------")

# Correlación del DataFrame
print("Correlación del DataFrame: ")
print(df.corr())
print("----------------------------")

# Cuenta los datos del DataFrame
print("Cuenta los datos del DataFrame:")
print(df.count())
print("----------------------------")

# Valor más alto de cada columna del DataFrame
print("Valor más alto de cada columna del DataFrame: ")
print(df.max())
print("----------------------------")

# Valor más bajo de cada columna del DataFrame
print("Valor más bajo de cada columna del DataFrame: ")
print(df.min())
print("----------------------------")

# Mediana de cada columna del DataFrame
print("Mediana de cada columna del DataFrame: ")
print(df.median())
print("----------------------------")

# Desviación estándar de cada columna del DataFrame
print("Desviación estándar de cada columna del DataFrame: ")
print(df.std())
print("----------------------------")

