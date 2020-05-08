# Los signos "# %%" sirve para evaluar celdas diferentes y utilizar python interactivo con una extensión en VScode

# Regresión Lineal Multiple
# Práctica: Modelo para predecir el precio de las casas en Boston en función 
# - Al número de habitaciones que cuenta la vivienda.
# - El tiempo que ha tenido ocupada.
# - La distancia que se encuentra la misma de los centros de trabajo de Boston.

# %%
########## LIBRERIAS A UTILIZAR ##########
# Se importan las librerías a utilizar
from sklearn import datasets, linear_model

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
########## PREPARAR LA DATA REGRESIÓN LINEAL MÚLTIPLE #########

# Seleccionamos solamente las columnas 5 a 7 del dataset
# C5: RM = numero de habitaciones. C6: AGE = Tiempo ocupada. C7: DIS = Distancia a centros de trabajos 
X_multiple = boston.data[:, 5:8]
print(X_multiple)

# Defino los datos correspondientes a las etiquetas
y_multiple = boston.target

# %%
########## IMPLEMENTACIÓN DE REGRESIÓN LINEAL MÚLTIPLE ###########

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, y_train, y_test = train_test_split(X_multiple, y_multiple, test_size=0.2)  # 80% to train and 20% to test

# Defino el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

# Entreno el modelo
lr_multiple.fit(X_train, y_train)

# %%
# Comparamos los datos testing con una predicción
import pandas as pd

# Realizo una predicción
Y_pred = lr_multiple.predict(X_test)

print('Comparación entre datos de test y predicción')

comparativa = {'Testing': y_test, 'Prediction': Y_pred}
df_comparativa = pd.DataFrame(comparativa)
print(df_comparativa.head(20))


# %%
########### DATOS DEL MODELO DE REGRESIÓN LINEAL SIMPLE #########
print('DATOS DEL MODELO DE REGRESIÓN LINEAL SIMPLE')
print()
print('Valor de la pendiente o coeficiente "a": ')
print(lr_multiple.coef_)
print('Valor de la intersección o coeficiente "b": ')
print(lr_multiple.intercept_)

# %%
print()
print('Precisión del modelo:')
print(lr_multiple.score(X_train, y_train))  # Si precision del modelo -> 1 mejor será el modelo

# %%
