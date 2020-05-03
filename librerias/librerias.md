# Librerias a utilizar en Machine Learning

Nota: Este es un material de apoyo personal que iré desarrollando en base a tutoriales e información que hay en internet, toda libre y gratuita. 

Cuando programas en python y te involucras en [Machine Learning](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico) las [librerias](https://es.wikipedia.org/wiki/Biblioteca_(inform%C3%A1tica)) mas importantes son las siguientes: 

- NumPy
- Pandas
- Matplotlib
- Scikit-Learn

Cada una de ellas las explicaré y citaré de donde las aprendí.

### [NumPy](https://numpy.org/)
[NumPy - Parte 1](https://youtu.be/WxJr143Os-A?list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3)

Es un paquete de python que significa **Numerical Python**. 

Librería principal para infomática científica.

- Proporciona potentes estructuras de datos.
- Implementa matrices y matrices multidimensaionales.
- Estas estructuras garantizan cálculos eficientes con matrices.

Array Numpy vs Listas Python:
- Ocupa menos espacio de memoria con NumPy que una Lista de Python. [Demostracion](link-a-comp_espacio.py) 
- Es mas rapido hacer calculos con arrays de NumPy que hacer calculos con listas y bucles en Python. [Demostracion](link-a-comp_velocidad.py)

[NumPy - parte 2](https://youtu.be/aqIMhiialq0?list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3)

Para hacer una matriz NumPy usamos la funcion: ```np.array()```

La demostracion de las funciones principales estan en el siguiente [link](https://github.com/francomanca93/MachineLearning/blob/master/librerias/numpy/arrays.py)

### [Pandas](https://pandas.pydata.org/)

[Pandas - Parte 1](https://youtu.be/gimfTyCNfGw?list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3)

Es una liberia para analisis de datos de python. Significa **Panel Data**

- Libreria de codigo abierto.
- Proporciona herramientas de análisis y manipulación de datos de alto rendimiento.

Utilizando esta libreria podemos lograr cinco pasos típicos en el procesamiento y análisis de datos:
- Cargar
- Preparar
- Manipular
- Modelar
- Analizar 
#### Series. Datos 1D
- Son estructuras de datos etiquetados y unidimensaionales. 
#### DataFrame. Datos 2D
- Son estructuras de datos etiquetados bidimensionales.
- Consta de tres componentes principales: 
    - Los datos
    - El índice. Puedes especificar su nombre
    - Las columnas. Puedes especificar su nombre
- Son los que mas se utilizan en Machine Learning.
#### Paneles. Datos 3D
- Son estructuras de datos etiquetados tridimensaionales. 

#### Características principales:

- Objeto DataFrame rápido y eficiente con indexación predeterminada y personalizada.
- Herramientas para cargar datos en objetos de datos en memoria desde diferentes formatos de archivo.
- Alineación de datos y manejo integrado de datos faltantes.
- Remodelación y giro de conjuntos de fechas.
- Etiquetado, corte, indexación y subconjunto de grandes conjuntos de datos.
- Las columnas de una estructura de datos se pueden eliminar o insertar.
- Agrupa por datos para agregación y transformaciones.
- Alto rendimiento de fusión y unión de datos.
- Funcionalidad de la serie de tiempo.

[Pandas - Parte 2](https://youtu.be/5S01zSgE9GA?list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3)

Pandas puede ser considerado como una version estructurada de matrices NumPy, en donde las filas y las columnas son identificadas con etiquetas. 

Pandas tambien proporciona para la manipulación de estructuras básicas de datos: 
- Herramientas
- Métodos
- Funcionalidad  

Ejemplos y explicacion de algunos metodos se encuentran en la carpeta [pandas](carpeta_de_pandas)

### [Matplotlib](https://matplotlib.org/)

Libreria de python para poder *presentar los datos* que se analicen con las librerias anteriores.

[Matplotlib - Parte 1](https://www.youtube.com/watch?v=2VeHtuqW3YY&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=8)

- Libreria de trazado utilizada para gráficos 2D.
- Tiene muchos valores predeterminados incorporados.
- Pasos básicos para trazar gráficos:
    1. Hacer incorporaciones necesarias (librerias, gráficos, datos, etc...)
    2. Preparar algunos datos.
    3. Trazar la funcion con la instrucción plot().
- Consideraciones al gráficar:
    - Figura. 
        - Ventana o página general donde se dibuja todo.
        - Se puede crear múltiples figuras independientes.
        - Una figura puede tener:
            - Subtitulos. Titulos centrado de la figura.
            - Leyenda
            - Barra de color
            - Otras. 
    - Ejes
        - Se agregan los ejes a la figura. 
        - Es el área en la que se grafican los datos con funciones como plot() y scatter(). 
        - Pueden tener etiquetas asociadas.
    - Eje X y Eje Y
        - Cada uno contiene su numeración.
        - Personalización de cada eje:
            - Título
            - Leyenda
            - Escalas
            - Líneas de la cuadrícula 
- Matplotlib, pyplot.
    - Matplotlib: Todo el paquete de visualización de datos de Python
    - pyplot: Módulo en el paquete matplotlib. El módulo proporciona una interfaz que permite crear figuras y ejes de forma implícita y automática para lograr la trama deseada.

NOTA: Los datos de Machine Learning para graficar en matplotlib deberán estar estructurados bajo la libreria de NumPy. 

[Matplotlib - Parte 2](https://www.youtube.com/watch?v=7ZjYXt5R1LU&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=9)

Gráficos más importantes:
    
- Diagrama de línea.
- Gráfico de barras.
- Histograma. 
- Gráfico de dispersión.
- Gráfico circular.
