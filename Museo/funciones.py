from clases import Usuario

# Lista simple de usuarios para autenticación
usuarios = [
    Usuario("jefe_restaura", "restaurador", "1234"),
    Usuario("director", "director", "abcd")
]

def autenticar(nombre, contrasena):
    for user in usuarios:
        if user.nombre == nombre and user.contrasena == contrasena:
            return user
    return None

def listar_obras(museo):
    for obra in museo.obras:
        estado = f" ({obra.estado})"
        print(f"{obra.nombre} de {obra.autor} - {obra.periodo}{estado}")
