from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QTextEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

from models.tarjeta import Tarjeta
class NuevaTarjeta(QDialog):
    def __init__(self, tarjeta=None):
        super().__init__()

        self.tarjeta = tarjeta

        self.setWindowTitle("Nueva Tarjeta")
        self.resize(400, 300)

        layout = QVBoxLayout()


        layout.addWidget(QLabel("Título"))
        self.txt_titulo = QLineEdit()
        layout.addWidget(self.txt_titulo)


        layout.addWidget(QLabel("Descripción"))
        self.txt_descripcion = QTextEdit()
        layout.addWidget(self.txt_descripcion)


        layout.addWidget(QLabel("Prioridad"))
        self.combo_prioridad = QComboBox()
        self.combo_prioridad.addItems(["Alta", "Media", "Baja"])
        layout.addWidget(self.combo_prioridad)


        layout_botones = QHBoxLayout()

        self.btn_crear = QPushButton("Crear")
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_crear.clicked.connect(self.crear_tarjeta)
        self.btn_cancelar.clicked.connect(self.reject)

        layout_botones.addWidget(self.btn_crear)
        layout_botones.addWidget(self.btn_cancelar)

        layout.addLayout(layout_botones)

        if self.tarjeta:
            self.setWindowTitle("Editar Tarjeta")

            self.txt_titulo.setText(self.tarjeta.titulo)
            self.txt_descripcion.setPlainText(self.tarjeta.descripcion)

            indice = self.combo_prioridad.findText(self.tarjeta.prioridad)
            self.combo_prioridad.setCurrentIndex(indice)

            self.btn_crear.setText("Guardar")

        self.setLayout(layout)
    
    def crear_tarjeta(self):

        titulo = self.txt_titulo.text()
        descripcion = self.txt_descripcion.toPlainText()
        prioridad = self.combo_prioridad.currentText()

        if self.tarjeta:

            self.tarjeta.titulo = titulo
            self.tarjeta.descripcion = descripcion
            self.tarjeta.prioridad = prioridad
            
            print(self.tarjeta.titulo)

        else:

            self.tarjeta = Tarjeta(
                titulo,
                descripcion,
                prioridad
            )

        self.accept()