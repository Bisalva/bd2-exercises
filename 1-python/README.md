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
  'multiples_palabras': 3
}
```
Pista: Puedes utilizar los métodos `strip()`, `rstrip()` o `lstrip()`

**9.** Crea una función llamada `filtrar_numeros(lista_numeros)` que reciba una lista de números del 1 al 20 y retorne tres listas: números pares, cuadrados de números impares, y números divisibles por 3. Realiza dos implementaciones: una usando ciclos y otra usando comprensión de listas.

# Ejercicios de trabajo autónomo

**1.** Crea una función `evaluar_nota(nota)` que reciba una nota entre 1.0 y 7.0 y retorne si está "Aprobado", "Reprobado", o "Aprobado con distinción" (reprobado < 4.0, aprobado >= 4.0, aprobado con distinción >= 6.0 ).

**2** Implementa nuevamente la función anterior utilizando manejo de excepciones. Para ello, puedes revisar las excepciones `ValueError`y `TypeError`, y determinar qué otras excepciones podrían ser pertinentes para el manejo de errores en este ejercicio.

**3.** Crea una función `contar_hasta(limite, parar_en)` que imprima números del 1 hasta `limite`, pero se detenga si encuentra el número `parar_en`.

**4.** Crea funciones para manejar una lista de frutas: `obtener_primera_y_ultima(frutas)`, `agregar_fruta(frutas, nueva_fruta)`, y `mostrar_frutas(frutas)` que muestren toda la lista.

**5.** Crea una función `crear_libro(titulo, autor, año, paginas)` que retorne un diccionario con la información del libro, y otra función `mostrar_libro(libro)` que imprima la información de forma ordenada.
 
**6.** Crea una función `calcular_total_compra(lista_compras)` que reciba una lista de productos con precios y retorne el costo total. También crea `agregar_producto(lista, nombre, precio)` para agregar productos a la lista.

**7.** Crea una función `calcular_gasto_promedio(gastos)` que reciba una lista de gastos diarios y retorne el promedio. Luego crea `analizar_gastos_semanales(semanas)` que use la función anterior para analizar múltiples semanas.

**8.** Crea una función `analizar_productos(productos)` que reciba una lista de productos:
```python
productos = [
    {"nombre": "Laptop", "precio": 800000, "categoria": "Tecnología"},
    {"nombre": "Mouse", "precio": 15000, "categoria": "Tecnología"},
    {"nombre": "Escritorio", "precio": 120000, "categoria": "Muebles"},
    {"nombre": "Silla", "precio": 80000, "categoria": "Muebles"}
]
```

La función debe retornar el precio promedio y el producto más caro.

**9.** Crea funciones para calcular estadísticas de un equipo de fútbol:

```python
partidos = [
    {"rival": "Equipo A", "goles_favor": 2, "goles_contra": 1},
    {"rival": "Equipo B", "goles_favor": 0, "goles_contra": 3},
    {"rival": "Equipo C", "goles_favor": 4, "goles_contra": 2},
    {"rival": "Equipo D", "goles_favor": 1, "goles_contra": 1}
]
```

Implementa `calcular_puntos(partidos)` (3 puntos por victoria, 1 por empate), `goles_totales(partidos)` y `mejor_resultado(partidos)`.

**10.** Crea una función `analizar_ventas(ventas_mensuales)` que reciba un diccionario de ventas:

```python
ventas_mensuales = {
    "Enero": [120000, 85000, 95000, 110000],
    "Febrero": [130000, 90000, 88000, 125000],
    "Marzo": [140000, 95000, 105000, 135000]
}
```
La función debe retornar un diccionario con el total de cada mes y cuál fue el mejor mes.

**11.** Crea una función `comparar_temperaturas(temperaturas)` que reciba un diccionario:

```python
temperaturas = {
    "Santiago": [22, 25, 28, 26, 24, 20, 18, 21, 23, 27],
    "Valparaíso": [18, 20, 22, 21, 19, 17, 16, 18, 20, 23]
}
```

Debe retornar cuál ciudad tiene mayor temperatura promedio y cuál tiene mayor variación.

**12.** Crea una función `procesar_mensajes(mensajes)` que reciba una lista como:

```python
mensajes = [
    "2024-01-15 10:30:45 Usuario conectado correctamente",
    "2024-01-15 10:31:12 Error al conectar usuario",
    "2024-01-15 10:31:45 Usuario desconectado",
    "2024-01-15 10:32:01 Error de sistema crítico"
]
```

Debe separar cada mensaje en fecha, hora y descripción, y contar cuántos errores hay.
