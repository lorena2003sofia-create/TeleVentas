from producto import Producto
from cliente import Cliente
from orden import OrdenCompra
from inventario import Inventario

inventario = Inventario()

p1 = Producto(1, "Laptop", 2500, 5)
p2 = Producto(2, "Mouse", 50, 20)

inventario.agregar_producto(p1)
inventario.agregar_producto(p2)

inventario.mostrar_catalogo()

cliente1 = Cliente("Ana", "ana@email.com")

orden1 = OrdenCompra(cliente1)
orden1.agregar_producto(p1)
orden1.agregar_producto(p2)

orden1.mostrar_orden()

cliente1.hacer_queja("Demora en entrega")

orden1.cancelar()
