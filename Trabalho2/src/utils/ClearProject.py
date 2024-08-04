import shutil
import os

class ClearProject:  
  @staticmethod
  def clear_cache():
      diretorios = [
          "gui",
          "models",
          "models/Objects2D",
          "utils"
      ]

      for diretorio in diretorios:
          path = os.path.join(diretorio, "__pycache__")
          if os.path.exists(path):
              shutil.rmtree(path)
              print(f"Pasta __pycache__ removida de src/{diretorio}")