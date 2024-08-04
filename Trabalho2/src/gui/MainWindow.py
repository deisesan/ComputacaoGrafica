from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsPolygonItem
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5.QtGui import QPolygonF
from typing import List
from models.Objects2D.Dot2D import Dot2D
from models.Objects2D.Line2D import Line2D
from models.Objects2D.Polygon2D import Polygon2D
from models.Viewport import Viewport
from models.Window import Window

class MainWindow(QMainWindow):
  def __init__(self, viewport: Viewport, window: Window,):
    super().__init__()
    self.scene = QGraphicsScene()
    self.view = QGraphicsView(self.scene)

    scene_dimension = QRectF(0, 0, 630, 470)
    self.scene.setSceneRect(scene_dimension)
    self.view.setSceneRect(scene_dimension)

    # Desabilitar barras de rolagem
    self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # Janela Genérica
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)
    layout.addWidget(self.view)

    # Tamanho fixo - Widget central
    widget.setFixedSize(630, 470)
    self.setCentralWidget(widget)

  def ShowObjects(self, dots: List[Dot2D], lines: List[Line2D], polygons: List[Polygon2D]):
    # Adicionando na View - Dots
    for dot in dots:
      dot_item = QGraphicsEllipseItem(dot.x, dot.y, 4, 4)
      dot_item.setBrush(Qt.green)
      self.scene.addItem(dot_item)

    # Adicionando na View - Lines
    for line in lines:
        line_item = QGraphicsLineItem(line.dot1.x, line.dot1.y, line.dot2.x, line.dot2.y)
        line_item.setPen(Qt.red)
        self.scene.addItem(line_item)

    # Adicionando na View - Polygons
    for polygon in polygons:
      polygon_dots = []
      for dot in polygon:
        dot_item = QPointF(dot.x, dot.y)
        polygon_dots.append(dot_item)
      final_polygon = QPolygonF(polygon_dots)
      polygon_item = QGraphicsPolygonItem(final_polygon)
      self.scene.addItem(polygon_item)
