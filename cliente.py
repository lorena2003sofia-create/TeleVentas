class Cliente:

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def hacer_queja(self, mensaje):
        print("Queja enviada:", mensaje)
