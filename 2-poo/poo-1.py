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
        self.notas = NOTAS
        
    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)
        
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
        
estudiante_dep_1 = EstudianteDeportista("María José", 27, "Ing. en contrucción", 
                                        [6.5], "Atletismo")
print(estudiante_dep_1.entrenar())