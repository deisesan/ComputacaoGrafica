import shutil
import os
from utils.ReadFile import ReadFile
from utils.WriteFile import WriteFile
from utils.GUI import GUI

if __name__ == "__main__":
  print("Olá, mundo!")
  readFile = ReadFile("../docs/entrada.xml")
  writeFile = WriteFile("../docs/saida.xml", readFile.viewport, readFile.window,
                        readFile.dots, readFile.lines, readFile.polygons)

  #Interface Gráfica 
  GUI()
  
  # Clear
  script_dir = os.path.dirname(os.path.abspath(__file__))
  pycache_path = os.path.join(script_dir, "utils", "__pycache__")
  shutil.rmtree(pycache_path)
  pycache_path = os.path.join(script_dir, "models", "__pycache__")
  shutil.rmtree(pycache_path)
