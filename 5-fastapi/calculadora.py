from fastapi import FastAPI

app = FastAPI(title="Calculadora")

# Parte 1: Endpoints con parámetros de ruta
@app.get("/sumar/{a}/{b}")
def sumar(a: float, b: float):
    return {"operacion": "suma", "a": a, "b": b, "resultado": a + b}

@app.get("/restar/{a}/{b}")
def restar(a: float, b: float):
    return {"operacion": "resta", "a": a, "b": b, "resultado": a - b}

@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: float, b: float):
    return {"operacion": "multiplicacion", "a": a, "b": b, "resultado": a * b}

@app.get("/dividir/{a}/{b}")
def dividir(a: float, b: float):
    if b == 0:
        return {"mensaje": "No se puede dividir por cero"}
    return {"operacion": "division", "a": a, "b": b, "resultado": a / b}


# Parte 2: Endpoints con parámetros de consulta
@app.get("/calcular")
def calcular(a: float, b: float, operacion: str = "suma"):
    if operacion == "suma":
        resultado = a + b
    elif operacion == "resta":
        resultado = a - b
    elif operacion == "multiplicacion":
        resultado = a * b
    elif operacion == "division":
        if b == 0:
            return {"mensaje": "No se puede dividir por cero"}
        resultado = a / b
    else:
        return {"mensaje": "Operación no válida"}

    return {"operacion": operacion, "a": a, "b": b, "resultado": resultado}


# Parte 3: Parámetros de ruta y de consulta combinados
@app.get("/potencia/{base}")
def potencia(base: float, exponente: int = 2):
    return {"base": base, "exponente": exponente, "resultado": base**exponente}
