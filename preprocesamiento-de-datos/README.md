# Análisis de datos
El análisis de datos o preprocesamiento de datos es preparar a los mismos para luego poderlos utilizarlos en los algoritmos de Machine Learning. 
- Los datos están en todas partes.
- Nos ayuda a responder preguntas utilizando datos.
- Nos ayuda a descubrir información útil con los datos.  

Una libreria es una coleccion de funciones y métodos que permiten realizar muchas acciones sin necesidad de escribir codigo aparte. Las principales están en este [link](https://github.com/francomanca93/MachineLearning/tree/master/librerias).

En la pagina una [Kaggle](https://www.kaggle.com/) podemos encontrar gran cantidad de datasets para prácticar. 

Se practicarán los pasos con un [dataframe de Titanic](https://www.kaggle.com/c/titanic/data).

- Pasos

1. Importar y exportar el conjunto de datos. [Práctica]()

    1. Importación de las librerias.
    ```
    import pandas as pd

    ó

    import pandas
    ```

    2. Cargar datos en Pandas.

        - Importar y exportar datos

            | Formato archivo | Importar(Leer) | Exportar(guardar) |
            | --- | --- | --- | --- |
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


