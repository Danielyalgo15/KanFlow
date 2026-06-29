import sys
from PyQt5.QtWidgets import QApplication
from views.main_window import MainWindow

app = QApplication(sys.argv)

ventana = MainWindow()
ventana.show()

sys.exit(app.exec_())