from datetime import date

class Obra:
    def __init__(self, nombre, autor, periodo, valor, fecha_creacion, fecha_ingreso):
        self.nombre = nombre
        self.autor = autor
        self.periodo = periodo
        self.valor = valor
        self.fecha_creacion = fecha_creacion
        self.fecha_ingreso = fecha_ingreso
        self.estado = "expuesta"  
        self.restauraciones = []
        self.cesion = None  

class Cuadro(Obra):
    def __init__(self, nombre, autor, periodo, valor, fecha_creacion, fecha_ingreso, estilo, tecnica):
        super().__init__(nombre, autor, periodo, valor, fecha_creacion, fecha_ingreso)
        self.estilo = estilo
        self.tecnica = tecnica

class Escultura(Obra):
    def __init__(self, nombre, autor, periodo, valor, fecha_creacion, fecha_ingreso, estilo, material):
        super().__init__(nombre, autor, periodo, valor, fecha_creacion, fecha_ingreso)
        self.estilo = estilo
        self.material = material

class OtroObjeto(Obra):
    pass  

class Restauracion:
    def __init__(self, tipo, fecha_inicio, fecha_fin=None):
        self.tipo = tipo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Museo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.obras = []
        self.museos_colaboradores = []

    def agregar_obra(self, obra):
        self.obras.append(obra)

    def valor_total_obras(self):
        return sum(obra.valor for obra in self.obras)

class Usuario:
    def __init__(self, nombre, rol, contrasena):
        self.nombre = nombre
        self.rol = rol  # "encargado", "restaurador", "director", "visitante"
        self.contrasena = contrasena
