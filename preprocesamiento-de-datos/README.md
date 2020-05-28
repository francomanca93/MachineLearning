# Análisis de datos
El análisis de datos o preprocesamiento de datos es preparar a los mismos para luego poderlos utilizarlos en los algoritmos de Machine Learning. 
- Los datos están en todas partes.
- Nos ayuda a responder preguntas utilizando datos.
- Nos ayuda a descubrir información útil con los datos.  

Una libreria es una coleccion de funciones y métodos que permiten realizar muchas acciones sin necesidad de escribir codigo aparte. Las principales están en este [link](https://github.com/francomanca93/MachineLearning/tree/master/librerias).

En la pagina una [Kaggle](https://www.kaggle.com/) podemos encontrar gran cantidad de datasets para prácticar. 

Se practicarán los pasos con un [dataframe de Titanic](https://www.kaggle.com/c/titanic/data).

- Pasos

1. Importar y exportar el conjunto de datos. [Práctica](https://github.com/francomanca93/MachineLearning/blob/master/preprocesamiento-de-datos/importar_exportar_datos_titanic.py)

    1. Importación de las librerias.
    ```
    import pandas as pd

    ó

    import pandas
    ```

    2. Cargar datos en Pandas.

        - Importar y exportar datos

            | Formato archivo | Importar(Leer) | Exportar(guardar) |
            | --- | --- | --- |
            | csv | `pandas.read_csv()`| `dataframe.to_csv()` |
            | json | `pandas.read_json()` | `dataframe.to_json()` |
            | excel | `pandas.read_excel()` | `dataframe.to_excel()` |
            | sql | `pandas.read_sql()` | `dataframe.to_sql()` |

        - Visualización de un dataframe
            ```
            dataframe.head(n)
            dataframe.tail(n)
            ```
        - Reemplazar cabecerar
            ```
            dataframe.columns
            ```

2. Explorando los datos.

Explorar los datos sirve para entender la data para planear como debemos continuar.
Pandas cuenta con varios métodos que pueden usarse para comprender el tipo de datos o para ver la distribución de datos dentro del conjunto de dados.

Datos que se manejan con Pandas:
- int y float: Tipo de datos numericos
- object: forma similar a la cadena de datos en Python.
- datetime: Tipo de datos muy útil para manejar series temporales de datos. (días, horas, etc.)

Razones para verificar tipos de datos:
- Panda puede asignar automáticamente tipos de datos.
- Las funciones matemáticas para Machine Learning solamente aceptan datos numéricos.

1. Conocer tipos de datos.
    ```
    dataframe.dtypes
    ```
    Nos devuelve una tabla con la informacion de cada tipo de dato de las columnas.

2. Análisis estadistico del dataframe.
    ```
    dataframe.describe()
    dataframe.describe(include="all")
    ```
Esta información nos puede decir si hay problemas matemáticos. Extremos atípicos, desviaciones, etc.

Aplicando el primer método podemos ver:
- count: se refiere al número de términos en la columna,
- mean: se refiere al valor promedio de la columna,
std: es la desviación estándar de la columna.

- También se muestra los valores máximo y mínimo, así como el límite de cada uno de los cuartiles.

Aplicando el primer método y modificando el atributo include a "all" podemos ver todo lo anterior mas lo siguiente:
- unique: esto se refiere al número de objetos distintos en la columna,
- top: es el dato más frecuente que se produce,
- freq: es la cantidad de veces que aparece el objeto “top” en la columna.

Algunos valores en la tabla se mostrarán como “NaN”, que significa “no es un número”, esto se debe a que esta métrica estadística particular no se puede calcular para ese específico tipo de datos de columna.