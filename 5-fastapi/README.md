# Actividad Práctica FastAPI: API de Calculadora

## Descripción

Construir una API REST de calculadora con FastAPI. Primero se crearán endpoints que realizan operaciones usando parámetros de ruta y de consulta.


## Parte 1: Endpoints con parámetros de ruta

Crea los siguientes endpoints `GET`. Los números `a` y `b` deben recibirse como parámetros de ruta de tipo `float`, y cada endpoint debe retornar un diccionario con la operación, los operandos y el resultado.

| Endpoint                | Operación      |
| ----------------------- | -------------- |
| `/sumar/{a}/{b}`        | `a + b`        |
| `/restar/{a}/{b}`       | `a - b`        |
| `/multiplicar/{a}/{b}`  | `a * b`        |
| `/dividir/{a}/{b}`      | `a / b`        |

Ejemplo:
```http
GET /sumar/4/2.5
```
```json
{"operacion": "suma", "a": 4.0, "b": 2.5, "resultado": 6.5}
```

En el caso de la división, si `b` es `0` el endpoint debe retornar:
```json
{"mensaje": "No se puede dividir por cero"}
```

## Parte 2: Endpoints con parámetros de consulta

### 2.1 Calculadora general
Crea un endpoint `GET /calcular` que reciba como **query parameters**:
- `a` (float, requerido)
- `b` (float, requerido)
- `operacion` (str, opcional, por defecto `"suma"`). Valores permitidos: `"suma"`, `"resta"`, `"multiplicacion"` y `"division"`.

Si la operación no es válida, debe retornar `{"mensaje": "Operación no válida"}`. También debe manejar la división por cero como en la Parte 2.

```http
GET /calcular?a=10&b=5
GET /calcular?a=10&b=5&operacion=division
GET /calcular?operacion=resta&b=5&a=10
```
## Parte 3: Combinando endpoints con parámetros de consulta y parámetros de ruta

### 3.1 Potencia
Crea un endpoint `GET /potencia/{base}` donde:
- `base` (float) es un parámetro de ruta.
- `exponente` (int) es un parámetro de consulta opcional con valor por defecto `2`.

```http
GET /potencia/3         
GET /potencia/2?exponente=10  
```
Debe retornar un JSON con la base, el exponente y el resultado.