from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

class MainWindow:
  def __init__(self):
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()