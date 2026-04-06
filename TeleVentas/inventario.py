class Inventario:

    def __init__(self):

        self.lista_productos=[]

    def agregar_producto(self,producto):

        self.lista_productos.append(producto)

    def mostrar_catalogo(self):

        print("\nCATALOGO:")

        for p in self.lista_productos:

            p.mostrar_info()
