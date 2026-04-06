class OrdenCompra:

    def __init__(self,cliente):

        self.cliente=cliente
        self.productos=[]

        self.estado="Activa"

    def agregar_producto(self,producto):

        self.productos.append(producto)

    def mostrar_orden(self):

        print("Orden de:",self.cliente.nombre)

        for p in self.productos:

            print("-",p.nombre)

    def cancelar(self):

        self.estado="Cancelada"

        print("Orden cancelada")
