import shutil
import os

class ClearProject:
  # Clear
  script_dir = os.path.dirname(os.path.abspath(__file__))
  parent_dir = os.path.dirname(script_dir)

  # pycache_path = os.path.join(parent_dir, "gui/__pycache__")
  # shutil.rmtree(pycache_path)
  pycache_path = os.path.join(script_dir, "__pycache__")
  shutil.rmtree(pycache_path)
  pycache_path = os.path.join(parent_dir, "models/__pycache__")
  shutil.rmtree(pycache_path)
  pycache_path = os.path.join(parent_dir, "models/Objects2D/__pycache__")
  shutil.rmtree(pycache_path)