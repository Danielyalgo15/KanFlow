from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)

from views.nueva_tarjeta import NuevaTarjeta
class DetalleTarjeta(QDialog):
    def __init__(self, tarjeta, widget):
        super().__init__()

        self.tarjeta = tarjeta
        self.widget = widget

        self.setWindowTitle("Detalle de la Tarjeta")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.lbl_titulo = QLabel(f"Título: {tarjeta.titulo}")
        layout.addWidget(self.lbl_titulo)

        self.lbl_descripcion = QLabel(f"Descripción: {tarjeta.descripcion}")
        layout.addWidget(self.lbl_descripcion)

        self.lbl_prioridad = QLabel(f"Prioridad: {tarjeta.prioridad}")
        layout.addWidget(self.lbl_prioridad)

        self.lbl_estado = QLabel(f"Estado: {tarjeta.estado}")
        layout.addWidget(self.lbl_estado)

        self.lbl_fecha = QLabel(f"Creada: {tarjeta.fecha_creacion}")
        layout.addWidget(self.lbl_fecha)

        self.lbl_historial = QLabel(
            "Historial:\n" + "\n".join(self.tarjeta.historial)
        )
        layout.addWidget(self.lbl_historial)

        layout_botones = QHBoxLayout()

        self.btn_editar = QPushButton("Editar")
        self.btn_mover = QPushButton("Mover")
        self.btn_eliminar = QPushButton("Eliminar")

        self.btn_editar.clicked.connect(self.editar_tarjeta)
        self.btn_mover.clicked.connect(self.mover_tarjeta)

        layout_botones.addWidget(self.btn_editar)
        layout_botones.addWidget(self.btn_mover)
        layout_botones.addWidget(self.btn_eliminar)

        layout.addLayout(layout_botones)

        self.btn_cerrar = QPushButton("Cerrar")
        self.btn_cerrar.clicked.connect(self.close)

        layout.addWidget(self.btn_cerrar)

        self.setLayout(layout)
        self.actualizar_datos()
        
    def editar_tarjeta(self):
        ventana = NuevaTarjeta(self.tarjeta)

        if ventana.exec_():
            self.actualizar_datos()
            self.accept()

    def mover_tarjeta(self):

        if self.tarjeta.estado == "Pendiente":
            siguiente_estado = "En Proceso"

        elif self.tarjeta.estado == "En Proceso":
            siguiente_estado = "Terminado"

        else:
            return

        cantidad = self.widget.main_window.contar_tarjetas(siguiente_estado)
        limite = self.widget.main_window.limite_wip[siguiente_estado]

        if cantidad >= limite:
            QMessageBox.warning(
                self,
                "Límite WIP",
                f"La columna '{siguiente_estado}' alcanzó su límite."
            )
            return

        self.tarjeta.mover()
        self.widget.actualizar()
        self.widget.main_window.mover_widget(self.widget)
        self.actualizar_datos()

    def actualizar_datos(self):
        self.lbl_titulo.setText(f"Título: {self.tarjeta.titulo}")
        self.lbl_descripcion.setText(f"Descripción: {self.tarjeta.descripcion}")
        self.lbl_prioridad.setText(f"Prioridad: {self.tarjeta.prioridad}")
        self.lbl_estado.setText(f"Estado: {self.tarjeta.estado}")
        self.lbl_fecha.setText(f"Creada: {self.tarjeta.fecha_creacion}")
        self.lbl_historial.setText(
            "Historial:\n" + "\n".join(self.tarjeta.historial)
        )
        if self.tarjeta.estado == "Terminado":
            self.btn_mover.setEnabled(False)
        else:
            self.btn_mover.setEnabled(True)