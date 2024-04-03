from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

class GUI:
  def __init__(self):
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()