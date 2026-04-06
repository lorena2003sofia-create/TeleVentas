from clases import Museo, Cuadro

def test_valor_total():
    museo = Museo("Museo Test")
    cuadro = Cuadro("Obra1", "Autor1", "Barroco", 500, "1600-01-01", "2023-01-01", "Clásico", "Óleo")
    museo.agregar_obra(cuadro)
    assert museo.valor_total_obras() == 500
    print("Prueba exitosa: valor total correcto")

test_valor_total()
