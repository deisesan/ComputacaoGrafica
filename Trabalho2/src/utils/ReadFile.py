from lxml import etree
from models.Viewport import Viewport
from models.Window import Window
from models.Objects2D.Dot2D import Dot2D
from models.Objects2D.Line2D import Line2D

class ReadFile:
  def __init__(self, filename: str):
    self.filename = filename
    self.tree = etree.parse(filename)

    # Busca dos Elementos -> Viewport
    viewport_xml = self.tree.find("./viewport")
    xvpmin = viewport_xml.find("vpmin").get("x")
    yvpmin = viewport_xml.find("vpmin").get("y")
    xvpmax = viewport_xml.find("vpmax").get("x")
    yvpmax = viewport_xml.find("vpmax").get("y")
    
    self.viewport = Viewport(xvpmin, yvpmin, xvpmax, yvpmax)

    # Busca dos Elementos -> Window
    window_xml = self.tree.find("./window")

    xwmin = window_xml.find("wmin").get("x")
    ywmin = window_xml.find("wmin").get("y")
    xwmax = window_xml.find("wmax").get("x")
    ywmax = window_xml.find("wmax").get("y")

    self.window = Window(xwmin, ywmin, xwmax, ywmax)

    # Busca dos Elementos -> Dots
    dots_xml = self.tree.findall("./ponto")

    dots = []

    for dot_xml in dots_xml:
        x = dot_xml.attrib['x']
        y = dot_xml.attrib['y']
        dot = Dot2D(x, y)
        dots.append(dot)

    self.dots = dots

    # Busca dos Elementos -> Lines
    lines_xml = self.tree.findall("./reta")

    lines = []

    for line_xml in lines_xml:
      x1 = line_xml[0].attrib['x']
      y1 = line_xml[0].attrib['y']

      dot1 = Dot2D(x1, y1)

      x2 = line_xml[1].attrib['x']
      y2 = line_xml[1].attrib['y']

      dot2 = Dot2D(x2, y2)

      line = Line2D(dot1, dot2)

      lines.append(line)

      self.lines = lines

    # Busca dos Elementos -> Polygons
    polygons_xml = self.tree.findall("./poligono")

    polygons = []

    for polygon_xml in polygons_xml:
      dots_polygon = []

      for dot_xml in polygon_xml.findall("./ponto"):
          x = dot_xml.attrib['x']
          y = dot_xml.attrib['y']
          dot = Dot2D(x, y)
          dots_polygon.append(dot)

      polygons.append(dots_polygon)

    self.polygons = polygons