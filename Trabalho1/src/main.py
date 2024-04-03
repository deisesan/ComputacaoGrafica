from PyQt5.QtWidgets import QApplication
import sys
from utils.ReadFile import ReadFile
from utils.WriteFile import WriteFile
from utils.ClearProject import ClearProject
from gui.MainWindow import MainWindow

if __name__ == "__main__":
  print("Olá, mundo!")
  readFile = ReadFile("../docs/entrada.xml")
  window = readFile.window
  viewport = readFile.viewport
  writeFile = WriteFile("../docs/saida.xml", viewport, window, readFile.dots, readFile.lines, readFile.polygons)

  # Cria Window sem configuração
  app = QApplication(sys.argv)
  main = MainWindow()
  main.resize(int(viewport.xvpmax), int(viewport.yvpmax))
  main.ShowObjects(writeFile.dots_transform, writeFile.lines_transform, writeFile.polygons_transform)
  main.show()
  
  # Limpeza das Pastas de Cache
  clear_project = ClearProject()
  clear_project.clear_cache()

  sys.exit(app.exec_())