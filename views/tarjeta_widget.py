from PyQt5.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QSizePolicy
from views.detalle_tarjeta import DetalleTarjeta


class TarjetaWidget(QFrame):
    def __init__(self, tarjeta, main_window):
        super().__init__()

        self.tarjeta = tarjeta
        self.main_window = main_window

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setFrameShape(QFrame.Box)

        layout = QVBoxLayout()

        self.lbl_titulo = QLabel(tarjeta.titulo)
        self.lbl_prioridad = QLabel(f"Prioridad: {tarjeta.prioridad}")

        layout.addWidget(self.lbl_titulo)
        layout.addWidget(self.lbl_prioridad)

        self.setLayout(layout)

    def actualizar(self):
        self.lbl_titulo.setText(self.tarjeta.titulo)
        self.lbl_prioridad.setText(f"Prioridad: {self.tarjeta.prioridad}")

    def mousePressEvent(self, event):

        ventana = DetalleTarjeta(self.tarjeta, self)

        if ventana.exec_():
            self.actualizar()