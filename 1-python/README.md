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

**5.** Utilizando la variable `mensaje`, crea un diccionario que almacene la cantidad de veces que aparece cada palabra. Luego, imprime cada palabra junto con su número de apariciones. Antes de comenzar, asegúrate de convertir todas las letras del mensaje a minúsculas.
```python
texto = "Python es genial ! Python es fácil de aprender y Python es muy usado"
```

**6.** Crea una función `crear_perfil_str(nombre, edad, altura, es_estudiante)` que reciba los datos de una persona y retorne un string formateado con toda la información usando `f-strings`.
```python
# Ejemplo de retorno
"Nombre: Juan, Edad: 25, Altura: 1.65, Es estudiante: Si"
```
**7.** Crea una función `crear_perfil_dict(persona)` que reciba un diccionario con los datos de una persona y retorne un string formateado con toda la información usando `f-strings`. El diccionario debe contener las siguientes claves: `nombre`,`edad`,`altura`. La clave `es_estudiante` es un valor booleano opcional, por lo que se debe verificar si existe, en caso de no existir deben indicar que no es estudiante.
```python
# Ejemplo de retorno
"Nombre: Juan, Edad: 25, Altura: 1.65, Es estudiante: Si"
```
**8.** Crea una función que retorne un diccionario con: una lista limpia de nombres (sin espacios extra, primera letra mayúscula). Y, además debe retornar cuenta cuántos elementos tienen más de una palabra. Utiliza la variable `nombres`:
```python
nombres = ["ana maría", "CARLOS PÉREZ", "  luis  ", "María José"]

# Ejemplo de retorno
{ 
  'nombres_limpios': ['Ana maría', 'Carlos pérez', 'Luis', 'María josé'], 
  'multiples_palabras': 4
}
```
Pista: Puedes utilizar los métodos `strip()`, `rstrip()` o `lstrip()`

**9.** Crea una función llamada `filtrar_numeros(lista_numeros)` que reciba una lista de números del 1 al 20 y retorne tres listas: números pares, cuadrados de números impares, y números divisibles por 3. Realiza dos implementaciones: una usando ciclos y otra usando comprensión de listas.