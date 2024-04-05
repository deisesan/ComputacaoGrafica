from PyQt5.QtWidgets import QApplication
import sys
from utils.ReadFile import ReadFile
from utils.WriteFile import WriteFile
from utils.ClearProject import ClearProject
from gui.MainWindow import MainWindow

if __name__ == "__main__":
  readFile = ReadFile("../docs/entrada.xml")
  viewport = readFile.viewport
  window = readFile.window
  writeFile = WriteFile("../docs/saida.xml", viewport, window, readFile.dots, readFile.lines, readFile.polygons)

  # Cria Window e Viewport 
  # Coloca os objetos na Viewport criada
  app = QApplication(sys.argv)
  main = MainWindow(viewport, window)
  main.ShowObjects(writeFile.dots_transform, writeFile.lines_transform, writeFile.polygons_transform)
  main.show()
  
  # Limpeza das Pastas de Cache
  # Se quiser que permaneça as pastas, só comentar essas duas linhas
  clear_project = ClearProject()
  clear_project.clear_cache()

  sys.exit(app.exec_())