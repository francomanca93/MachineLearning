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