class Producto:

    def __init__(self,codigo,nombre,precio,cantidad):

        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

    def mostrar_info(self):

        print(self.codigo,self.nombre,"$",self.precio,"Stock:",self.cantidad)
