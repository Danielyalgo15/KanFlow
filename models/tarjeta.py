from datetime import datetime


class Tarjeta:
    def __init__(self, titulo, descripcion, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad

        self.estado = "Pendiente"

        self.fecha_creacion = datetime.now()
        self.fecha_inicio = None
        self.fecha_finalizacion = None