
from utils.ReadFile import ReadFile
from utils.WriteFile import WriteFile
from utils.ClearProject import ClearProject
from gui.MainWindow import MainWindow

if __name__ == "__main__":
  print("Olá, mundo!")
  readFile = ReadFile("../docs/entrada.xml")
  writeFile = WriteFile("../docs/saida.xml", readFile.viewport, readFile.window, readFile.dots, readFile.lines, readFile.polygons)

  #Interface Gráfica 
  MainWindow()
  
  # Limpeza das Pastas de Cache
  ClearProject()
  