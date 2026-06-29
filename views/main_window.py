from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KanFlow")
        self.resize(1000, 600)

        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.layout_principal = QVBoxLayout()
        self.central.setLayout(self.layout_principal)

        self.titulo_tablero = QLabel("Tablero: Universidad")
        self.layout_principal.addWidget(self.titulo_tablero)

        self.layout_contenido = QHBoxLayout()
        self.layout_principal.addLayout(self.layout_contenido)

        self.panel_izquierdo = QGroupBox("Opciones")
        self.layout_panel = QVBoxLayout()
        self.panel_izquierdo.setLayout(self.layout_panel)
        self.layout_principal.setStretch(0, 0)
        self.layout_principal.setStretch(1, 1)
        self.layout_contenido.addWidget(self.panel_izquierdo)
        self.layout_contenido.setStretch(0, 1)
        self.panel_izquierdo.setStyleSheet("""
            QGroupBox {
                border: 2px solid black;
                margin-top: 10px;
                font-weight: bold;
            }
        """)

        self.panel_derecho = QGroupBox("Tablero")
        self.layout_tablero = QHBoxLayout()
        self.panel_derecho.setLayout(self.layout_tablero)
        self.layout_contenido.addWidget(self.panel_derecho)
        self.layout_contenido.setStretch(1, 3) 
        self.panel_derecho.setStyleSheet("""
            QGroupBox {
                border: 2px solid black;
                margin-top: 10px;
                font-weight: bold;
            }
        """)

        self.col_pendiente = QGroupBox("Pendiente")
        self.col_proceso = QGroupBox("En Proceso")
        self.col_terminado = QGroupBox("Terminado")
 
        self.layout_pendiente = QVBoxLayout()
        self.layout_proceso = QVBoxLayout()
        self.layout_terminado = QVBoxLayout()

        self.col_pendiente.setLayout(self.layout_pendiente)
        self.col_proceso.setLayout(self.layout_proceso)
        self.col_terminado.setLayout(self.layout_terminado)

        self.layout_tablero.addWidget(self.col_pendiente)
        self.layout_tablero.addWidget(self.col_proceso)
        self.layout_tablero.addWidget(self.col_terminado)
        self.layout_tablero.setStretch(0, 1)
        self.layout_tablero.setStretch(1, 1)
        self.layout_tablero.setStretch(2, 1)