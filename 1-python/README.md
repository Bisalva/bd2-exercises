# Ejercicios de Python

**1.** Crea una lista con 10 notas usando valores entre 1.0 y 7.0. Recorre la lista con un ciclo for para calcular el promedio, la nota mínima y la nota máxima. Imprime los tres resultados usando `f-strings`, por ejemplo: `Promedio: 4.82, Nota mínima: 2.1, Nota máxima: 6.9`.

**2.** Dado un texto, recórrelo carácter por carácter con un ciclo for para contar cuántas vocales contiene (a, e, i, o, u), sin diferenciar entre mayúsculas y minúsculas. Además, cuenta cuántas palabras tiene utilizando el método `.split()`. Finalmente, imprime un resumen usando un `f-string`, por ejemplo: `El texto tiene 5 palabras y 12 vocales`.

**3.** Recorre la lista de diccionarios y, para cada estudiante, determina si aprobó o reprobó considerando que se aprueba con una nota mayor o igual a 4.0. Además, calcula el promedio del curso y cuenta cuántos estudiantes aprobaron. Imprime por cada estudiante un mensaje usando un `f-string` indicando su nombre, su nota y si aprobó o reprobó. 
```python
estudiantes = [
    {"nombre": "Ana", "nota": 5.5},
    {"nombre": "Pedro", "nota": 3.2},
    {"nombre": "Maria", "nota": 6.8},
    {"nombre": "Juan", "nota": 3.9},
    {"nombre": "Sofia", "nota": 4.0},
]
```

**4.** Implementa el ejercicio anterior utilizando comprensión de listas.

**5.** Utilizando la variable `mensaje`, crea un diccionario que almacene cuántas veces aparece cada palabra e imprime cada palabra junto con su cantidad de apariciones. Asegúrate de pasar todas las letras a minúscula antes de empezar el ejercicio.
```python
texto = "Python es genial ! Python es fácil de aprender y Python es muy usado"
```
