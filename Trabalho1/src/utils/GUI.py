from PyQt5.QtWidgets import QApplication, QMainWindow

class GUI_Window(QMainWindow):
    def __init__(self):
        super().__init__()

class GUI:
  def __init__(self):
    app = QApplication([])
    window = GUI_Window()
    window.show()
    app.exec_()