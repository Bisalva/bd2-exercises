# Listas 

numeros = [1,2,3,4,5, "uno","dos","tres","cuatro"]

for numero in numeros:
    print(numero)
    
lista_mixta = [5,"hola mundo", True, [1,2,3,4], numeros]
for elemento in lista_mixta:
    print(elemento)
print(lista_mixta[1])
print(numeros[0:3])

numeros.append(10)
numeros.insert(3, "Nuevo elemento")
numeros.append(3)
print(numeros)

numeros.insert(3, True)
numeros.remove(3)
print(numeros)
print(lista_mixta)

numeros_pares = [2,4,6,8]
numeros_impares = [1,3,5,7]
nueva_lista = numeros_impares + numeros_pares
print(nueva_lista)

print(numeros)
print(numeros.count(1))
print(f"La cantidad de elementos de la lista numeros es: {len(numeros)}")
print(nueva_lista)
nueva_lista.sort() # método inplace, modifica la variable
print(nueva_lista)
# print(sorted(nueva_lista))
# print(sorted(numeros))


palabras = ["Hola","como","estas"]
print(sorted(palabras))

for idx, palabra in enumerate(palabras):
    print(idx,palabra)


a = [1,2,3]
b = a
print(a,b)
b.append(90)
print(a,b)
print(id(a), id(b))

c = a.copy()
c.append(24)
print(a,c)

nums = [1,2,3,4,5]
cuadrados = []
for num in nums:
    cuadrados.append(num**2)
print(cuadrados)
            # elemento_a_guardar   coleccion a iterar
cuadrados = [num**2 for num in nums]
print(cuadrados)
cuadrados_impares = []

for num in nums:
    if(num%2 == 1):
        cuadrados.append(num**2)
    
cuadrados_impares = [num**2 for num in nums if num%2 ==1]

# Diccionarios
persona = {"nombre": "Camila", "edad": 25, "ciudad":"Punta Arenas",
           130: True, "hijos":{"nombre":"Juan", "edad":12}
           }
print(persona)
print(persona["nombre"])
#print(persona["Pais"]) #Error
print(persona.get("Pais"))
print(persona.get("Pais","Chile"))
print(f"Nombre: {persona['nombre']}\nEdad: {persona['edad']}\nciudad: {persona['ciudad']}")
print(f"Nombre {persona['nombre']}, hijos {persona['hijos']}")

persona_con_hijos = {"nombre":"Juan",
                     "hijos":[{"nombre": "José"}, {"nombre":"Camilo"}]}
persona_sin_hijos = {"nombre": "Alejandra"}

print(f"Nombre: {persona_con_hijos['nombre']}, Hijos: {len(persona_con_hijos['hijos'])}")

print(len(persona_sin_hijos.get("hijos",[])))
print(len(persona_con_hijos.get("hijos",[])))
if len(persona_sin_hijos.get("hijos",[])) == 0 :
    print(f"Nombre {persona_sin_hijos['nombre']}, Hijos: No")
else:
    print(f"Nombre {persona_sin_hijos['nombre']}, Hijos: Si")
    
# Operador ternario
# valor_true if condicion else valor_false
print(f"Hijos: {'Si 'if len(persona_sin_hijos.get('hijos',[])) > 0 else 'No'}")
print(persona)
del persona[130]
persona.pop("hijos")
print(persona)

print(f"Claves del diccionario: {persona.keys()}")
print(f"Valores del diccionario: {persona.values()}")
print(f"Clave-valor: {persona.items()}")

for clave in persona.keys():
    print(clave, persona[clave])
    
for clave, valor in persona.items():
    print(f"{clave}={valor}")
    

# Ejercicios
## 3. Recorre la lista de diccionarios y, para cada estudiante, determina si aprobó o reprobó
## considerando que se aprueba con una nota mayor o igual a 4.0. 
## Además, calcula el promedio del curso y cuenta cuántos estudiantes aprobaron. 
## Imprime por cada estudiante un mensaje usando un f-string indicando su nombre, su nota y si aprobó o reprobó.

estudiantes = [
    {"nombre": "Ana", "nota": 5.5},
    {"nombre": "Pedro", "nota": 3.2},
    {"nombre": "Maria", "nota": 6.8},
    {"nombre": "Juan", "nota": 3.9},
    {"nombre": "Sofia", "nota": 4.0},
]

cantidad_estudiantes_aprobados = 0
suma_notas = 0
for estudiante in estudiantes:
    # print(f"Estudiante: {estudiante}")
    suma_notas = suma_notas + estudiante["nota"]
    if(estudiante["nota"]>=4.0):
        print(f"Nombre: {estudiante['nombre']}, nota {estudiante['nota']} (Aprobado)")
        cantidad_estudiantes_aprobados = cantidad_estudiantes_aprobados + 1
    else:
        print(f"Nombre: {estudiante['nombre']}, nota {estudiante['nota']} (Reprobado)")
promedio = suma_notas / len(estudiantes)
print(f"Cantidad de aprobados: {cantidad_estudiantes_aprobados}\nPromedio:{promedio}")


## 4. Implementa el ejercicio anterior utilizando comprensión de listas.
### imprimir nombre del estudiante , estado
resultados = [f"Nombre: {estudiante['nombre']}, nota {estudiante['nota']} (Aprobado)"
              if estudiante["nota"] >=4.0
              else 
              f"Nombre: {estudiante['nombre']}, nota {estudiante['nota']} (Reprobado)"
              for estudiante in estudiantes]
resultados = [f"Nombre: {estudiante['nombre']}, nota {estudiante['nota']}  {'Aprobado' if estudiante['nota']>=4.0 else 'Reprobado'}" 
              for estudiante in estudiantes]

for resultado in resultados:
    print(resultado)
### calcular el promedio
# sum(promedio)
promedio = sum([estudiante["nota"] for estudiante in estudiantes]) / len(estudiantes)
# print(promedio)

### Indicar la cantidad de estudiantes aprobados
aprobados = [estudiante for estudiante in estudiantes if estudiante["nota"]>= 4.0]
# print(f"La cantidad de estudiantes aprobados es {len(aprobados)}")


## 5. Utilizando la variable mensaje, crea un diccionario que almacene 
## la cantidad de veces que aparece cada palabra. 
## Luego, imprime cada palabra junto con su número de apariciones. 
## Antes de comenzar, asegúrate de convertir todas las letras del mensaje a minúsculas.
texto = "Python es genial ! python es fácil de aprender y PYTHON es muy usado"

palabras = texto.lower().split(" ")
print(palabras)
conteo = {}
# {"python": 1}
# {"python":1 , "es":1}
# {"python": 2}
for palabra in palabras:
    #print(conteo)
    # opción 1
    if palabra in conteo:
        conteo[palabra] = conteo[palabra]+1 
        # conteo[palabra] += 1
    else:
        conteo[palabra] = 1
    # opción 2:
    # conteo[palabra] = conteo["palabra"].get(palabra,0) +1
print(conteo)
for palabra,cantidad in conteo.items():
    print(f"{palabra} aparece {cantidad} veces")