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

        self.historial = [
            f"Pendiente - {self.fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')}"
        ]
    def mover(self):

        if self.estado == "Pendiente":
            self.estado = "En Proceso"
            self.fecha_inicio = datetime.now()
            self.historial.append(
                f"En Proceso - {self.fecha_inicio.strftime('%d/%m/%Y %H:%M:%S')}"
            )

        elif self.estado == "En Proceso":
            self.estado = "Terminado"
            self.fecha_finalizacion = datetime.now()
            self.historial.append(
                f"Terminado - {self.fecha_finalizacion.strftime('%d/%m/%Y %H:%M:%S')}"
            )