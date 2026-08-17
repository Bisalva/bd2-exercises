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