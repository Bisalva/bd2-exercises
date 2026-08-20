# Ejercicios de Programación Orientada a Objetos en Python

## 1. Producto

### 1.1 Definición de clases
Crea una clase `Producto` con los siguientes atributos:
- `nombre` (string)
- `precio` (float) 
- `stock` (int)

Implementa los métodos:
- `__init__(self, nombre, precio, stock)`
- `mostrar_info(self)` - imprime la información del producto
- `aplicar_descuento(self, porcentaje)` - reduce el precio según el porcentaje
- `vender(self, cantidad)` - reduce el stock si hay suficiente, sino imprime error

```python
# Ejemplo de uso:
producto = Producto("Laptop", 800000, 5)
producto.mostrar_info()
producto.aplicar_descuento(10)
producto.vender(2)
```

### 1.2. Productos especializados
A partir de la clase Producto creada en el ejercicio anterior, extiende el programa incorporando herencia y polimorfismo.

Crea dos clases que hereden de `Producto`:

- `ProductoElectronico`: Añade el atributo garantia (en meses).
- `ProductoAlimenticio`: Añade el atributo fecha_vencimiento.

Ambas clases deben utilizar el constructor de `Producto` para inicializar los atributos comunes.

Además, modifica el método `mostrar_info()` para que cada tipo de producto muestre su información de manera diferente. Por ejemplo:

- `ProductoElectronico` debe mostrar también la garantía.
- `ProductoAlimenticio` debe mostrar también la fecha de vencimiento.

### 1.3 Protección de atributos de la clase Producto
Modifica la clase `Producto` para que el atributo `stock` no pueda ser modificado directamente desde fuera de la clase. Implementa métodos que permitan:
- consultar el stock disponible;
- aumentar el stock;
- reducir el stock mediante el método `vender()`.

### 1.4 Lista de productos
Crea una lista que contenga objetos de distintos tipos de productos y recorre la lista llamando a `mostrar_info()` para cada uno.
