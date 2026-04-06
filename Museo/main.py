from clases import Museo, Cuadro, Escultura
from funciones import autenticar, listar_obras

def main():
    # Crear museo
    museo = Museo("Museo Principal")

    # Crear obras
    cuadro1 = Cuadro("La noche estrellada", "Van Gogh", "Postimpresionismo", 1000, "1889-06-01", "2020-01-10", "Impresionismo", "Óleo")
    escultura1 = Escultura("David", "Miguel Ángel", "Renacimiento", 2000, "1504-01-01", "2021-05-01", "Renacentista", "Mármol")
    
    museo.agregar_obra(cuadro1)
    museo.agregar_obra(escultura1)

    # Autenticación simple
    usuario = autenticar("director", "abcd")
    if usuario:
        print(f"Bienvenido {usuario.nombre} ({usuario.rol})")
        listar_obras(museo)
        print(f"Valor total de las obras: ${museo.valor_total_obras()}")
    else:
        print("Usuario o contraseña incorrecta")

if __name__ == "__main__":
    main()
