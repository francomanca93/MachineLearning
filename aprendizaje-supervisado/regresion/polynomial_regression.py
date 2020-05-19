# Los signos "# %%" sirve para evaluar celdas diferentes y utilizar python interactivo con una extensión en VScode

# Regresión polinomial
# Práctica: Modelo para predecir el precio de las casas en Boston en función 
# - Al número de habitaciones que cuenta la vivienda.

# %%
########## LIBRERIAS A UTILIZAR ##########
# Se importan las librerías a utilizar
from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt

########## PREPARAR LA DATA ##########
# Importamos los datos de la misma librería de scikit-learn
boston = datasets.load_boston()
print(boston)
print("----------------------------")

# %%
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
########## PREPARAR LA DATA REGRESIÓN POLINOMIAL #########

# Seleccionamos solamente la columna 6 del dataset (empieza de 0)
# C5: RM = numero de habitaciones.
X_p = boston.data[:, np.newaxis, 5]

# Defino los datos correspondientes a las etiquetas
y_p = boston.target

# Graficamos los datos correspondientes
plt.scatter(X_p, y_p)
plt.show()

# %%
########## IMPLEMENTACIÓN DE REGRESIÓN POLINOMIAL ###########

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_p, y_p, test_size=0.2)  # 80% to train and 20% to test

from sklearn.preprocessing import PolynomialFeatures

# Se define el grado del polinomio
poli_reg = PolynomialFeatures(degree=2)

# Se transforma las características existentes en características de mayor grado.
X_train_poli = poli_reg.fit_transform(X_train_p)
X_test_poli = poli_reg.fit_transform(X_test_p)

# Defino el algoritmo a utilizar
pr = linear_model.LinearRegression()

# Entreno el modelo
pr.fit(X_train_poli, y_train_p)

# %%
# Comparamos los datos testing con una predicción
import pandas as pd

# Realizo una predicción
Y_pred_pr = pr.predict(X_test_poli)

print('Comparación entre datos de test y predicción')

comparativa = {'Testing': y_test_p, 'Prediction': Y_pred_pr}
df_comparativa = pd.DataFrame(comparativa)
print(df_comparativa.head(20))

# %%
# Graficamos los datos junto con el modelo
plt.scatter(X_test_p, y_test_p)
plt.plot(X_test_p, Y_pred_pr, color='red', linewidth=3)
plt.show()

# %%
########### DATOS DEL MODELO DE REGRESIÓN POLINOMIAL #########
print('DATOS DEL MODELO DE REGRESIÓN LINEAL SIMPLE')
print()
print('Valor de la pendiente o coeficiente "a": ')
print(pr.coef_)
print('Valor de la intersección o coeficiente "b": ')
print(pr.intercept_)

# %%
print()
print('Precisión del modelo:')
print(pr.score(X_train_poli, y_train_p))  # Si precision del modelo -> 1 mejor será el modelo

# %%
