# Funciones
def saludar():
    print("Hola mundo")

def suma(num1,num2):
    valor_suma = num1+num2
    return valor_suma

print(suma(4,6))
print(suma(num1 = 7, num2=4))
print(suma(num2=2, num1=8))

def suma_y_resta(num1: int | float ,num2: int | float) -> int | float:
    """
    Función que suma y resta dos numeros
    args:
    num1 (int | float): Número a sumar o restar
    num2 (int | float): Numero a sumar o restar
    
    return:
    int | float: Resultado de la suma
    int | float: Resultado de la resta
    """
    
    return num1+num2, num1-num2
print(suma_y_resta(7,3))
suma, resta = suma_y_resta(6,2)
print(f"la suma de 6 y 2 es {suma} y la resta es {resta}")
# help(suma_y_resta)

def agregar_elemento(lista):
    lista.append(199)
    
numeros = [1,2,3,4,5,6]
print(numeros)
agregar_elemento(numeros)
print(numeros)


# Excepciones
print(f"{'-'*9} Excepciones {'-'*9}")
num1 = 6
num2 = "a"
try:
    print(num1/int(num2))
except ZeroDivisionError as e:
    print(f"No se puede dividir por cero ({e}) ")
except TypeError as e:
    print("Tipo de dato invalido")
except NameError as e:
    print(f"Variable no definida ({e})")
except Exception as e:
    print(f"ocurrio un error {num1=} {num2=} ({e})")
    

# Ejercicios
## 6. Crea una función crear_perfil(nombre, edad, altura, es_estudiante) 
## que reciba los datos de una persona y retorne un string formateado
## con toda la información usando f-strings.
def crear_perfil(nombre, edad, altura, es_estudiante):
                        #valor_True condicion valor_False
    mensaje_estudiante = f"{'Si' if es_estudiante else 'No'}"
    if es_estudiante:
        print("Si")
        mensaje_estudiante = "Si"
    else:
        mensaje_estudiante = "No"
        
    print(mensaje_estudiante)
    return f"Nombre: {nombre}\nEdad: {edad}\n Altura: {altura}\n Estudiante: {mensaje_estudiante}"

print(crear_perfil("Juan",25,1.60, False))

## 7. Crea una función crear_perfil_dict(persona) que reciba un diccionario 
## con los datos de una persona y retorne un string formateado con toda
## la información usando f-strings. 
## El diccionario debe contener las siguientes claves: nombre,edad,altura. 
## La clave es_estudiante es un valor booleano opcional, por lo que se debe verificar si existe, 
## en caso de no existir deben indicar que no es estudiante.

def crear_perfil_dict(persona):
    nombre = persona.get("nombre") #persona["nombre"]
    edad = persona.get("edad")
    altura = persona.get("altura")
    es_estudiante = persona.get("es_estudiante",False) 
    mensaje_estudiante = f"{'Si' if es_estudiante else 'No'}"
    
    return f"Nombre: {nombre}\nEdad: {edad}\nAltura: {altura}\nEs estudiante:{mensaje_estudiante}"

persona = {"nombre":"Camila", "edad":23, "altura":1.77, "es_estudiante":False}
print(crear_perfil_dict(persona))