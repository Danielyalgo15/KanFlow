import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

ventana = QLabel("¡Bienvenido a KanFlow!")
ventana.resize(300, 100)
ventana.show()

sys.exit(app.exec_())