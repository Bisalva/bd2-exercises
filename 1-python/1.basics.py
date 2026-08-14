print("Hola mundo")
print('Hola mundo')
# Variables
# Esto es un comentario
# Esto es otro comentario

asignatura = "Base de datos II" # Esto es un comentario
semestre = 4
true = True
false = False
print(type(asignatura), type(semestre), type(true))
semestre = "Cuarto semestre"
print(type(semestre))

# Condicionales
numero = -64
if(numero>20):
    print("El número es mayor a 20")
else:
    print("El número es menor o igual a 20")
print("HOLA") # Esto siempre se ejecuta porque esta fuera del bloque del if

nota = 3.9
if nota>=5.5:
    print("Aprobado con distincion")
elif(nota >=4.0): #else if
    print("Aprobado")
else:
    print("Reprobo")
    
if(nota != 1.0):
    print("La nota es diferente a la nota mínima")

asistencia = 60
aprobado = False
if(nota>=4.0 and asistencia>=70):
    print("Estudiante se encuentra aprobado")   
    aprobado = True 
elif(nota>=4.0 or asistencia>=70):
    print("No cumple con uno de los requisitos")
else:
    print("Estudiante reprobado")

if(not aprobado):
    print("Reprobado")

# Ciclos
print(numero)
while(numero<=0):
    print(numero)
    numero = numero +15
    
# for(i=0;i<n; i++)
for i in range(10):
    print(i)
    
animales = ["gato","perro","panda","pajaro","suricata", 43]
for animal in animales:
    print(animal)
    
for letra in asignatura:
    print(letra)

print("Ciclo con números del 0 al 9")
for i in range(10):
    print(i)
    if(i == 5):
        break

if("perro" in animales):
    print("Perro esta dentro de la lista")
if("ratón" not in animales):
    print("Ratón no se encuentra en la lista")

# Strings
saludo = "Hola"
print(saludo)

# saludo[2] = "L" # Error
saludo = "Hola"
saludo_completo = saludo + " estudiantes de " + asignatura
print(saludo_completo)

print(f"{saludo} estudiantes de {asignatura}")
num1 = 5
num2 = 8
print(f"multiplicación: {num1 * num2}, división {num1/num2}")

print(asignatura)
print(asignatura[0:5])
print(asignatura[5:10])
print(asignatura[5:])
print(asignatura[-1])

print(asignatura.upper())
print(asignatura.lower())
nombre = "       Camila             "
print(f"[{nombre}]")
print(f"[{nombre.strip()}]")
print(f"[{nombre.rstrip()}]")
print(f"[{nombre.lstrip()}]")
nombre = "Camila$$$$"
print(nombre.strip("$"))

print(asignatura)
print(asignatura.split(" "))
print(asignatura.replace("II","I"))

numero = 3.1415
print(round(numero,2))

# Ejercicios
print("-------- Ejercicios -------- ")
# 1. Crea una lista con 10 notas usando valores entre 1.0 y 7.0. 
# Recorre la lista con un ciclo for para calcular el promedio, la nota mínima y la nota máxima. 
# Imprime los tres resultados usando f-strings, por ejemplo: Promedio: 4.82, Nota mínima: 2.1, Nota máxima: 6.9.
notas = [4.5, 6.2, 3.8, 5.0, 2.1, 6.9, 4.4, 5.5, 3.9, 6.0]
promedio = 0
nota_baja = notas[0] #10 
nota_maxima = notas[0]
for nota in notas:
    promedio = promedio +nota
    if(nota <= nota_baja):
        nota_baja = nota
    if(nota > nota_maxima):
        nota_maxima = nota
print(f"Promedio: {promedio / len(notas)}, Nota mínima {nota_baja}, Nota máxima: {nota_maxima}")

promedio = sum(notas) / len(notas)
nota_minima = min(notas)
nota_maxima = max(notas)
print(f"Promedio: {round(promedio,1)}, Nota mínima {nota_minima}, Nota máxima: {nota_maxima}")


# 2. Dado un texto, recórrelo carácter por carácter con un ciclo for para 
# contar cuántas vocales contiene (a, e, i, o, u), 
# sin diferenciar entre mayúsculas y minúsculas. 
# Además, cuenta cuántas palabras tiene utilizando el método .split().
# Finalmente, imprime un resumen usando un f-string, por ejemplo: El texto tiene 5 palabras y 12 vocales

texto = "Python es un lenguaje de programacion muy utilizado hoy en dia"
contador_vocales = 0
for caracter in texto.lower():
    # Opción 1
    # if caracter in "aeiou":
    #     contador_vocales = contador_vocales + 1
    # Opción 2
    # if caracter == "a":
    #     contador_vocales = contador_vocales +1
    # if caracter == "e":
    #     contador_vocales = contador_vocales +1
    # if caracter == "i":
    #     contador_vocales = contador_vocales +1
    # if caracter == "o":
    #     contador_vocales = contador_vocales +1
    # if caracter == "u":
    #     contador_vocales = contador_vocales +1
    # Opción 3
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
         contador_vocales = contador_vocales +1
    
palabras = texto.split(" ")
print(palabras)
print(f"{texto}\n El texto tiene {len(palabras)} palabras y  {contador_vocales} vocales")

