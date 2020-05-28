### Explorando los datos
import pandas

url = 'preprocesamiento-de-datos/data/titanic-train-espanol.csv'

dataframe = pandas.read_csv(url)

print("Conocer tipos de datos")
print(dataframe.dtypes)
print("----------------------------")

print("Análisis estadístico de los datos")
print(dataframe.describe())
print("----------------------------")
print("Análisis estadístico de los datos incluyendo todos los datos")
print(dataframe.describe(include='all'))
print("----------------------------")

print("Visualizar los datos de las filas")
print(dataframe.info)