from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QPushButton,
    QMessageBox,
    QComboBox,
    QLineEdit
)
from views.nueva_tarjeta import NuevaTarjeta
from views.tarjeta_widget import TarjetaWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KanFlow")
        self.resize(1000, 600)
        self.tarjetas = []
        self.limite_wip = {
            "Pendiente": 3,
            "En Proceso": 2,
            "Terminado": 999
        }
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

        self.btn_nueva = QPushButton("Nueva Tarjeta")
        self.layout_panel.addWidget(self.btn_nueva)
        self.btn_nueva.clicked.connect(self.nueva_tarjeta)

        self.btn_metricas = QPushButton("Ver métricas")
        self.btn_metricas.clicked.connect(self.ver_metricas)
        self.layout_panel.addWidget(self.btn_metricas)

        self.layout_panel.addWidget(QLabel("Filtrar por estado"))
        self.combo_filtro = QComboBox()
        self.combo_filtro.addItems([
            "Todos",
            "Pendiente",
            "En Proceso",
            "Terminado"
        ])
        self.combo_filtro.currentTextChanged.connect(self.filtrar_tarjetas)
        self.layout_panel.addWidget(self.combo_filtro)

        self.layout_panel.addWidget(QLabel("Filtrar por prioridad"))
        self.combo_prioridad = QComboBox()
        self.combo_prioridad.addItems([
            "Todas",
            "Alta",
            "Media",
            "Baja"
        ])
        self.combo_prioridad.currentTextChanged.connect(self.filtrar_tarjetas)
        self.layout_panel.addWidget(self.combo_prioridad)

        self.layout_panel.addWidget(QLabel("Filtrar por fecha"))
        self.txt_fecha = QLineEdit()
        self.txt_fecha.setPlaceholderText("dd/mm/yyyy")
        self.txt_fecha.textChanged.connect(self.filtrar_tarjetas)
        self.layout_panel.addWidget(self.txt_fecha)

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
        self.layout_pendiente.addStretch()
        self.layout_proceso.addStretch()
        self.layout_terminado.addStretch()

        self.layout_tablero.addWidget(self.col_pendiente)
        self.layout_tablero.addWidget(self.col_proceso)
        self.layout_tablero.addWidget(self.col_terminado)
        self.layout_tablero.setStretch(0, 1)
        self.layout_tablero.setStretch(1, 1)
        self.layout_tablero.setStretch(2, 1)

    def nueva_tarjeta(self):
        if self.contar_tarjetas("Pendiente") >= self.limite_wip["Pendiente"]:
            QMessageBox.warning(
                self,
                "Límite WIP",
                "La columna 'Pendiente' alcanzó su límite."
            )
            return
        
        ventana = NuevaTarjeta()

        if ventana.exec_():

            tarjeta = ventana.tarjeta
            widget = TarjetaWidget(tarjeta, self)
            self.tarjetas.append(widget)

            self.layout_pendiente.insertWidget(
                self.layout_pendiente.count() - 1,
                widget
            )
    def mover_widget(self, widget):

        self.layout_pendiente.removeWidget(widget)
        self.layout_proceso.removeWidget(widget)
        self.layout_terminado.removeWidget(widget)

        if widget.tarjeta.estado == "Pendiente":
            self.layout_pendiente.insertWidget(
                self.layout_pendiente.count() - 1,
                widget
            )

        elif widget.tarjeta.estado == "En Proceso":
            self.layout_proceso.insertWidget(
                self.layout_proceso.count() - 1,
                widget
            )

        elif widget.tarjeta.estado == "Terminado":
            self.layout_terminado.insertWidget(
                self.layout_terminado.count() - 1,
                widget
            )
        self.filtrar_tarjetas()

    def filtrar_tarjetas(self):

        estado = self.combo_filtro.currentText()
        prioridad = self.combo_prioridad.currentText()
        fecha = self.txt_fecha.text().strip()

        for widget in self.tarjetas:

            cumple_estado = (
                estado == "Todos"
                or widget.tarjeta.estado == estado
            )

            cumple_prioridad = (
                prioridad == "Todas"
                or widget.tarjeta.prioridad == prioridad
            )

            cumple_fecha = (
                fecha == ""
                or widget.tarjeta.fecha_creacion.strftime("%d/%m/%Y") == fecha
            )

            if cumple_estado and cumple_prioridad and cumple_fecha:
                widget.show()
            else:
                widget.hide()
    
    def contar_tarjetas(self, estado):
        cantidad = 0
        for widget in self.tarjetas:
            if widget.tarjeta.estado == estado:
                cantidad += 1
        return cantidad
    
    def ver_metricas(self):
        total = len(self.tarjetas)
        pendientes = 0
        proceso = 0
        terminadas = 0
        ciclo_total = 0
        lead_total = 0
        tarjetas_ciclo = 0
        tarjetas_lead = 0

        for widget in self.tarjetas:

            if widget.tarjeta.estado == "Pendiente":
                pendientes += 1

            elif widget.tarjeta.estado == "En Proceso":
                proceso += 1

            elif widget.tarjeta.estado == "Terminado":
                terminadas += 1

            ciclo = widget.tarjeta.tiempo_ciclo()
            if ciclo:
                ciclo_total += ciclo.total_seconds()
                tarjetas_ciclo += 1

            lead = widget.tarjeta.lead_time()
            if lead:
                lead_total += lead.total_seconds()
                tarjetas_lead += 1

        if tarjetas_ciclo > 0:
            promedio_ciclo = ciclo_total / tarjetas_ciclo
        else:
            promedio_ciclo = 0

        if tarjetas_lead > 0:
            promedio_lead = lead_total / tarjetas_lead
        else:
            promedio_lead = 0

        QMessageBox.information(
            self,
            "Métricas",
            f"""Total de tarjetas: {total}

    Pendientes: {pendientes}
    En Proceso: {proceso}
    Terminadas: {terminadas}

    Tiempo de ciclo promedio: {promedio_ciclo:.2f} segundos
    Lead Time promedio: {promedio_lead:.2f} segundos"""
        )