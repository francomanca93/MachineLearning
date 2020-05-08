
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

### [Regresión lineal múltiple](https://www.youtube.com/watch?v=wMg1HU6pfnk&list=PLJjOveEiVE4Dk48EI7I-67PEleEC5nxc3&index=17)

En la vida real una variable que queremos predecir depende de múltiples variables independientes, de aca surge este algoritmo de regresión lineal múltiple.

- Se manejan múltiples:
    - Variables independientes que contribuyen a la variable dependiente.
    - Coeficientes, por ende más compleja debido a las variables añadidas.
- Matemáticamente: y = a1 * x1 + a2 * x2 + an * xn + b
    - y = Variable dependiente
    - a1...n = coeficientes
    - x1...n = variables independientes
    - b = intersección

No se incluyen todas las variables independientes para empezar a estudiar, para luego minimizar la función de error.
- ¿Como analizamos que variables elegir?
    - Construir una matriz de correlación. 
        - En esta se incluyen todas las variables independientes y la variable dependiente. 
        - Con esto el valor de correlación sabemos que variable es significativa y por ende elegimos esa para hacer el estudio.
    - ¿Porque hacemos esto? 
        - Agregar todas las variables o muchas no significa que la regresión sea mejor u ofrezca mejor predicción. 
        - Ajuste excesivo: Agregar mas variables independientes que pueden contribuir al aumento del error. 
            - ¿Porque? Porque las variables independientes estan potencialmente relacionadas entre sí. Esto se llama *multicolinealidad*.  