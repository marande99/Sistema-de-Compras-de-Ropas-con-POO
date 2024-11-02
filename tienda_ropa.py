from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio, talla):
        self._nombre = nombre   
        self._precio = precio   
        self._talla = talla     

    @abstractmethod
    def mostrar_detalle(self):
        pass

# Clase Camisa que hereda de Producto
class Camisa(Producto):
    def __init__(self, nombre, precio, talla, tipo_manga):
        super().__init__(nombre, precio, talla)
        self.tipo_manga = tipo_manga

    def mostrar_detalle(self):
        print(f"Camisa: {self._nombre}, Precio: ${self._precio}, Talla: {self._talla}, Manga: {self.tipo_manga}")

# Clase Pantalon que hereda de Producto
class Pantalon(Producto):
    def __init__(self, nombre, precio, talla, tipo_material):
        super().__init__(nombre, precio, talla)
        self.tipo_material = tipo_material

    def mostrar_detalle(self):
        print(f"Pantalón: {self._nombre}, Precio: ${self._precio}, Talla: {self._talla}, Material: {self.tipo_material}")

# Clase Zapato que hereda de Producto
class Zapato(Producto):
    def __init__(self, nombre, precio, talla, tipo_cierre):
        super().__init__(nombre, precio, talla)
        self.tipo_cierre = tipo_cierre

    def mostrar_detalle(self):
        print(f"Zapato: {self._nombre}, Precio: ${self._precio}, Talla: {self._talla}, Cierre: {self.tipo_cierre}")

# Clase Tienda que gestiona una lista de productos
class Tienda:
    def __init__(self):
        self.productos = []

    # Método para agregar un producto a la tienda
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para mostrar todos los productos en la tienda
    def mostrar_productos(self):
        print("Productos disponibles en la tienda:")
        for producto in self.productos:
            producto.mostrar_detalle()

# Bloque principal del programa
if __name__ == "__main__":
    # Crear instancia de la tienda
    tienda = Tienda()

    # Crear instancias de productos
    camisa = Camisa("Camisa de algodón", 29.99, "M", "larga")
    pantalon = Pantalon("Pantalón jeans", 49.99, "L", "denim")
    zapato = Zapato("Zapato de cuero", 89.99, "42", "cordones")

    # Agregar productos a la tienda
    tienda.agregar_producto(camisa)
    tienda.agregar_producto(pantalon)
    tienda.agregar_producto(zapato)

    # Mostrar los productos en la tienda
    tienda.mostrar_productos()
