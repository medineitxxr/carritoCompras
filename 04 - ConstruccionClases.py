class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        pass

class ItemCarrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        pass

    def __str__(self):
        pass

class Carrito:
    def __init__(self, producto:Producto, item:ItemCarrito):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        pass

    def eliminar_producto(self, producto):
        pass

    def total(self):
        pass

    def ver_resumen(self):
        pass

class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.carrito = Carrito()

    def __str__(self):
        pass
