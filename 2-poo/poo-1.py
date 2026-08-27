class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.año_nacimiento = 2026 - edad

    def __repr__(self):
        return f"{self.nombre} --> {self.edad}"
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    def presentarse(self):
        return f"Hola soy {self.nombre}, tengo {self.edad} años y nací en el año {self.año_nacimiento}"

persona_1 = Persona(nombre = "Juan Pérez", edad = 20)
persona_2 = Persona("Camila Yañez", 25)

print(persona_1)
print(persona_1.presentarse())
print(persona_1.saludar())
print(persona_2.presentarse())

class Estudiante(Persona):
    def __init__(self, nombre,edad, carrera, NOTAS):
        super().__init__(nombre,edad)
        self.carrera = carrera
        #self.notas = NOTAS # atributo publico
        #self._notas = NOTAS # atributo protegido
        self.__notas = NOTAS # atributo privado
    
    def __str__(self):
        return f"{self.nombre} --> {self.__notas} "
    
    def calcular_promedio(self):
        return sum(self.__notas) / len(self.__notas)
    
    def presentarse(self):
        return f"Hola soy {self.nombre}, soy estudiante de la carrera de {self.carrera} y tengo {self.edad}"
    
    def agregar_nota(self, nota):
        self.__notas.append(nota)

    def vaciar_notas(self):
        self.__notas.clear()
        
estudiante_1 = Estudiante("Ana", 22, "Ing. en computación", [5,6.2,4.3, 5.5])
print(estudiante_1)      
print(estudiante_1.calcular_promedio()) 
print(estudiante_1.presentarse()) 

class Profesor(Persona):
    def __init__(self, nombre, edad, departamento, SUELDO ):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self.salario = SUELDO
        
    def describir(self):
        return f"Soy {self.nombre} y soy profesor de {self.departamento}"
    
    def presentarse(self):
        return f"Hola, soy {self.nombre}, y soy profesor del departamento de {self.departamento}"
profesor_1 = Profesor("Javier Pérez", 45, "Departamento de Computación", 2500000)

print(profesor_1)
print(profesor_1.describir())
#print(estudiante_1.describir())

class Deportista:
    def __init__(self, deporte):
        self.deporte = deporte
    def entrenar(self):
        return f"{self.deporte}: entrenamiento en progreso"
    
class EstudianteDeportista(Estudiante, Deportista):
    def __init__(self, nombre, edad, carrera, notas, deporte):
        Estudiante.__init__(self, nombre, edad,carrera, notas)
        Deportista.__init__(self,deporte)
    
    def presentarse(self):
        return f"Hola soy {self.nombre}, estudio {self.carrera} y entreno {self.deporte}"
        
        
        
estudiante_dep_1 = EstudianteDeportista("María José", 27, "Ing. en contrucción", 
                                        [6.5], "Atletismo")
print(estudiante_dep_1.entrenar())
print(f"{'-'*30}")
print(estudiante_1.presentarse())
print(profesor_1.presentarse())
print(estudiante_dep_1.presentarse())

print(f"{'-'*50}")
estudiante_2 = Estudiante("Carlos", 25, "Ing. en electricidad", [5,6.2,4.3, 5.5])
print(estudiante_2.presentarse())
print(estudiante_2.calcular_promedio())
# estudiante_2.__notas = [7.0] # No se debe hacer nunca porque se rompe el encapsulamiento
print(estudiante_2.calcular_promedio())
print(estudiante_2.__dict__)
estudiante_2.agregar_nota(7.0)
print(estudiante_2.__dict__)
estudiante_2.vaciar_notas()
print(estudiante_2.__dict__)
