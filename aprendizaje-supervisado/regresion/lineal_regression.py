# %%  # Los signos "# %%" sirve para evaluar celdas diferentes y utilizar python interactivo con una extensión en VScode

# Regresión Lineal simple

########## LIBRERIAS A UTILIZAR ##########
# Si importan las librerías a utilizar
import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

########## PREPARAR LA DATA ##########
# Importamos los datos de la misma librería de scikit-learn
boston = datasets.load_boston()
print(boston)
print("----------------------------")

########## ENTENDIMIENTO DE LA DATA #########

# Verifico la información contenida en el dataset
print("Información en el dataset: ")
print(boston.keys())
print("----------------------------")

# Verifico las características del dataset
print("Caracteristicas del dataset: ")
print(boston.DESCR)
print("----------------------------")

# Verifico la cantidad de datos que hay en los dataset
print("Cantidad de datos: ")
print(boston.data.shape)
print("----------------------------")

# Verifico la información de las columnas
print("Nombres columnas: ")
print(boston.feature_names)
print("----------------------------")

# %%
########## PREPARAR LA DATA REGRESIÓN LINEAL SIMPLE #########

# Seleccionamos solamente la columna 5 del dataset
X = boston.data[:, np.newaxis, 5]

# Defino los datos correspondientes a las etiquetas
y = boston.target

# Graficamos los datos correspondientes
plt.scatter(X, y)
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()

# %%
########## IMPLEMENTACIÓN DE REGRESIÓN LINEAL SIMPLE ###########

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 80% to train and 20% to test

# Defino el algoritmo a utilizar
lr = linear_model.LinearRegression()

# Entreno el modelo
lr.fit(X_train, y_train)

# %%
# Comparamos los datos testing con una predicción
import pandas as pd

# Realizo una predicción
Y_pred = lr.predict(X_test)

print('Comparación entre datos de test y predicción')

comparativa = {'Testing': y_test, 'Prediction': Y_pred}
df_comparativa = pd.DataFrame(comparativa)
print(df_comparativa.head(20))

# %%
# Graficamos los datos junto con el modelo
plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=2)
plt.title('Regresión lineal simple')
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()

# %%
########### DATOS DEL MODELO DE REGRESIÓN LINEAL SIMPLE #########
print('DATOS DEL MODELO DE REGRESIÓN LINEAL SIMPLE')
print()
print('Valor de la pendiente o coeficiente "a": ')
print(lr.coef_)
print('Valor de la intersección o coeficiente "b": ')
print(lr.intercept_)
print()
print('La ecuación del modelo es igual a:')
print('y = ', lr.coef_, ' + ( x * ', lr.intercept_, ')')

# %%
print()
print('Precisión del modelo:')
print(lr.score(X_train, y_train))