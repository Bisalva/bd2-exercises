from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hola():
    return "Mi primera aplicación."

@app.get("/saludar")
def saludar():
    return "Hola!"

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return f"Hola {nombre}"

@app.get("/saludo2")
def saludo2(nombre:str = "Estudiantes"):
    return {"mensaje":f"Hola {nombre}"}
    #return f"Hola {nombre}"
