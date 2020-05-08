
# Algoritmos de regresión. Teoría

## Regresión lineal

### [Regresión lineal simple](https://www.youtube.com/watch?v=5TcA5M5z4sA&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=15&t=1s)

- Método estadístico que nos permite resumir y estudiar las relaciones entre dos variables continuas cuantitativas.
- Técnica paramétrica utilizada para predecir variables continuas, dependientes, dado un conjunto de variables independientes. 
- Matemáticamente: y = a*x + b
    - y = Variable dependiente
    - a = pendiente
    - x = variable independiente
    - b = intersección

- Objetivo: Minimizar la distancia entre todos nuestros datos y la linea, el cual sería nuestro error.
    - Error: Es inevitable, por lo tanto querremos reducirlo hasta lo que mas se pueda.
    - ¿Como?: Usando el criterio *Mínimos cuadrados* para reducir el error, el cual busca el mejor valor para los coeficientes de regresión
    - ¿Porque usamos *Mínimos cuadrados*?
        - Utiliza un error cuadrado. Tiene buenas propiedades matemáticas. 
        - Fácil de analizar. 
        - Más rápido computacionalmente.
        - Más fácil interpretarlos. 
    - Coeficientes a cálcular (las fórmulas matemáticas las podemos encontrar en el video que dirige en hiperviculo del titulo. ):
        - Pendiente a
        - Intersección b

El rendimiento del modelo depende de las suposiciones
- Suposiciones.
    - Existe relación lineal (si cambia variable independiente cambia variable dependiente linealmente)
    - Existe una relación aditiva (las variables a analizar son independientes de otras variables)
    - No debe haber correlación entre las variables independientes.
    - Los términos de error deben poseer varianza constante, ni deben correlacionarse. (esto afecta a los coeficientes del modelo)
    - La variable dependiente y los términos de error deben tener una distribución normal.