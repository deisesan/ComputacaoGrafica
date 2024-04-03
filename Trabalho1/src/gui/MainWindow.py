from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPolygonF
from typing import List
from models.Objects2D.Dot2D import Dot2D
from models.Objects2D.Line2D import Line2D
from models.Objects2D.Polygon2D import Polygon2D

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

  def ShowObjects(self, dots: List[Dot2D], lines: List[Line2D], polygons: List[Polygon2D]):
    self.scene = QGraphicsScene()
    self.view = QGraphicsView(self.scene)
    self.setCentralWidget(self.view)

    for dot in dots:
      dot_item = QGraphicsEllipseItem(dot.x, dot.y, 4, 4)
      dot_item.setBrush(Qt.green)
      self.scene.addItem(dot_item)

    for line in lines:
        line_item = QGraphicsLineItem(line.dot1.x, line.dot1.y, line.dot2.x, line.dot2.y)
        line_item.setPen(Qt.red)
        self.scene.addItem(line_item)

    for polygon in polygons:
      polygon_dots = []
      for dot in polygon:
        dot_item = QPointF(dot.x, dot.y)
        polygon_dots.append(dot_item)
      final_polygon = QPolygonF(polygon_dots)
      polygon_item = QGraphicsPolygonItem(final_polygon)
      self.scene.addItem(polygon_item)
