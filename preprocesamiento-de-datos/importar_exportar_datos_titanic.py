### Importar las librerías
import pandas

url = 'preprocesamiento-de-datos/data/titanic-train.csv'

dataframe = pandas.read_csv(url)

print("Las primeras filas")
print(dataframe.head(5))
print("----------------------------")
print("Las últimas filas")
print(dataframe.tail(5))
print("----------------------------")

cabecera = ['ID', 'Sobreviviente', 'Clase', 'Nombre', 'Sexo', 'Edad', 'Hermanos', 'Hijos', 'Ticket', 'Tarifa', 'Cabina','Enbarque']
dataframe.columns = cabecera
print("Las primeras filas con cabeceras en español")
print(dataframe.head(5))
print("----------------------------")

ruta_a_guardar = 'preprocesamiento-de-datos/data/titanic-train-espanol.csv'
dataframe.to_csv(ruta_a_guardar)

