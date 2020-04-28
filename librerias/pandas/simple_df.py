# Simple Data Frame

import numpy as np
import pandas as pd

print("------------- Creando Data Frame simple 1 -------------")
print()
array = np.array([
    ['', 'Columna1', 'Columna2'],
    ['Fila1', 11, 22],
    ['Fila2', 33, 44]
])
dataFrame = pd.DataFrame(
    data=array[1:, 1:], 
    index=array[1:, 0], 
    columns=array[0, 1:])
print(dataFrame)

# ------------- Creando Data Frame simple 2 -------------
print("------------- Creando Data Frame simple 2 -------------")
print()
df = pd.DataFrame(np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)]))
print("DataFrame: ")
print(df)
