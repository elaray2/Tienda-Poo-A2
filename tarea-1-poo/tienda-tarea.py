class cliente:
    def __init__(self, id, nombres, telefono, direccion, email):
        self.id = id
        self.nombres = nombres
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
    
    def __str__(self):
        return f"Datos del cliente: {self.nombres}, {self.telefono}, {self.direccion}, {self.email}"


class VentaDetalle:
    def __init__(self, producto, cantidad, precio, impuesto):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.impuesto = impuesto
    
    def totalItem(self):
        impuesto_porcentaje = self.impuesto / 100
        impuesto_valor = self.precio * impuesto_porcentaje
        total_item = self.precio + impuesto_valor
        return total_item


class Venta:
    def __init__(self, id, fecha, cliente):
        self.id = id
        self.fecha = fecha
        self.cliente = cliente
        self.subtotal = 0
        self.impuesto = 0
        self.total = 0
        self.detalle = []
    
    def agregarDetalle(self, Venta_detalle):
        self.detalle.append(Venta_detalle)
        self.subtotal += Venta_detalle.totalItem()
        self.impuesto += Venta_detalle.totalItem() * (Venta_detalle.impuesto / 100)
        self.total = self.subtotal + self.impuesto


class Producto():
    def __init__(self, nombre, tipo, precioBase):
        self.nombre = nombre
        self.tipo = tipo
        self.precioBase = precioBase

    def __str__(self):
        return f"Datos del producto: {self.nombre}, {self.tipo}, {self.precioBase}"

    
    def calcularPrecioFinal(self):

        impuesto = 0
        
        if self.tipo == "papeleria":
            impuesto = 16
        elif self.tipo == "supermercado":
            impuesto = 4
        elif self.tipo == "drogueria":
            impuesto = 12
        
        precioFinal = self.precioBase + (self.precioBase * (impuesto / 100))
        return precioFinal


class Inventario:
    def __init__(self):
        self.productos = []
    
    def CantidadProductos(self):
        return len(self.productos)
    
    def CantidadAbastecimiento(self):
        count = 0
        for producto in self.productos:
            if producto.cantidadActual < producto.cantidadMinimaAbastecimiento:
                count += 1
        return count
    
    def visualizar(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}")
            print(f"Tipo: {producto.tipo}")
            print(f"Cantidad actual: {producto.cantidadActual}")
            print(f"Cantidad mínima para abastecimiento: {producto.cantidadMinimaAbastecimiento}")
            print(f"Precio base de venta por unidad: {producto.precioBase}")
    
    def abastecer(self, nombre, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.cantidadActual += cantidad
                break
        else:
            print("El producto no está en el inventario")

class Tipo:
    def __init__(self, id):
        self.id = id
        self.nombre = ["papeleria", "supermercado", "drogueria"]

class EstadisticaVenta:
    def __init__(self, ventas):
        self.ventas = ventas
    
    def CantidadTotalVentas(self):
        return len(self.ventas)
    
    def CantidadPromedioUnidad(self):
        pass
    
    def productoMasVendido(self):
        if len(self.ventas) > 0:
            productos_vendidos = {}

    
    def productoMenosVendido(self):
        if len(self.ventas) > 0:
            productos_vendidos = {}

#AGRAGACIÓN
cliente1 = cliente(7, "Ariel Lara", 44098958, "avenue 5th", "ariel12@gmail.com")
#print(cliente1.id, "", cliente1.nombres, "", cliente1.direccion)
print(cliente1.__str__())

#ASOCIACIÓN
producto1 = Producto("resma hojas A4", "papeleria", 5.99)
print(producto1.__str__())

venta1 = Venta(45, "24-05-2023", "Ariel Lara")
print(venta1.__str__())
