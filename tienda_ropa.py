from abc import ABC, abstractmethod

# Clase abstracta Producto
class Producto(ABC):
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @abstractmethod
    def mostrar_info(self):
        pass

    def obtener_precio(self):
        return self._precio

# Clase Ropa que hereda de Producto
class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        print(f"Ropa: {self._nombre}, Precio: ${self._precio}, Talla: {self._talla}, Tela: {self._tipo_tela}")

# Clase Camisa que hereda de Ropa
class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_manga):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_manga = tipo_manga

    def mostrar_info(self):
        print(f"Camisa: {self._nombre}, Precio: ${self._precio}, Talla: {self._talla}, Tela: {self._tipo_tela}, Manga: {self._tipo_manga}")

# Clase Pantalon que hereda de Ropa
class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_corte):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_corte = tipo_corte

    def mostrar_info(self):
        print(f"Pantalón: {self._nombre}, Precio: ${self._precio}, Talla: {self._talla}, Tela: {self._tipo_tela}, Corte: {self._tipo_corte}")

# Clase Zapato que hereda de Producto
class Zapato(Producto):
    def __init__(self, nombre, precio, talla, tipo_material):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_material = tipo_material

    def mostrar_info(self):
        print(f"Zapato: {self._nombre}, Precio: ${self._precio}, Talla: {self._talla}, Material: {self._tipo_material}")

# Clase Tienda que maneja los productos
class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Productos disponibles en la tienda:")
        for producto in self.productos:
            producto.mostrar_info()

# Clase Carrito que almacena productos seleccionados
class Carrito:
    def __init__(self):
        self.items = []

    def agregar_al_carrito(self, producto):
        self.items.append(producto)
        print(f"{producto._nombre} añadido al carrito.")

    def mostrar_resumen(self):
        print("Resumen de la compra:")
        total = 0
        for item in self.items:
            item.mostrar_info()
            total += item.obtener_precio()
        print(f"Total a pagar: ${total}")

# Función principal
if __name__ == "__main__":
    tienda = Tienda()

    # Agregar productos a la tienda
    tienda.agregar_producto(Camisa("Camisa Casual", 29.99, "M", "algodón", "larga"))
    tienda.agregar_producto(Pantalon("Jeans", 49.99, "L", "denim", "recto"))
    tienda.agregar_producto(Zapato("Zapatos de Cuero", 89.99, "42", "cuero"))

    # Mostrar productos de la tienda
    tienda.mostrar_productos()

    # Crear carrito de compras
    carrito = Carrito()

    # Interacción de usuario simulada
    carrito.agregar_al_carrito(tienda.productos[0])  # Añadir la camisa
    carrito.agregar_al_carrito(tienda.productos[1])  # Añadir el pantalón

    # Mostrar el resumen de la compra
    carrito.mostrar_resumen()
