from lxml import etree
from typing import List
from utils.Convert import Convert
from models.Viewport import Viewport
from models.Window import Window
from models.Objects2D.Dot2D import Dot2D
from models.Objects2D.Line2D import Line2D
from models.Objects2D.Polygon2D import Polygon2D

class WriteFile:
    def __init__(self, filename: str, viewport: Viewport, window: Window, 
                dots: List[Dot2D], 
                lines: List[Line2D], 
                polygons: List[Polygon2D]):
        self.filename = filename
        self.convert = Convert(window, viewport)

        # Aplicando Transformada - Dots
        dots_transform = []

        for dot in dots:
            xv, yv = self.convert.transform(dot.x, dot.y)
            dot_v = Dot2D(xv, yv)
            dots_transform.append(dot_v)   

        # Aplicando Transformada - Lines
        lines_transform = []

        for line in lines:
            xv1, yv1 = self.convert.transform(line.dot1.x, line.dot1.y)
            xv2, yv2 = self.convert.transform(line.dot2.x, line.dot2.y)

            dot_v1 = Dot2D(xv1, yv1)
            dot_v2 = Dot2D(xv2, yv2)

            line = Line2D(dot_v1, dot_v2)

            lines_transform.append(line)
        
        # Aplicando Transformada - Polygons
        polygon_transform = []

        for polygon in polygons:
            dots_polygon_transform = []

            for dot in polygon:
                xv, yv = self.convert.transform(dot.x, dot.y)
                dot_v = Dot2D(xv, yv)
                dots_polygon_transform.append(dot_v)

            polygon_transform.append(dots_polygon_transform)

        # Escrita no arquivo XML
        tree_out = etree.Element("dados")

        # Criando elemento xml para Dots
        dots_transform_xml = etree.SubElement(tree_out, "pontos")

        for dot in dots_transform:
            etree.SubElement(dots_transform_xml, "ponto", x=str(dot.x), y=str(dot.y))

        # Criando o elemento para as linhas transformadas
        lines_transform_xml = etree.SubElement(tree_out, "retas")

        for line in lines_transform:
            line_xml = etree.SubElement(lines_transform_xml, "reta")
            etree.SubElement(line_xml, "ponto", x=str(line.dot1.x), y=str(line.dot1.y))
            etree.SubElement(line_xml, "ponto", x=str(line.dot2.x), y=str(line.dot2.y))

        # Criando o elemento para os polígonos transformados
        polygon_transform_xml = etree.SubElement(tree_out, "poligonos")

        for polygon in polygon_transform:
            poligono_xml = etree.SubElement(polygon_transform_xml, "poligono")
            for dot in polygon:
                etree.SubElement(poligono_xml, "ponto", x=str(dot.x), y=str(dot.y))

        tree = etree.ElementTree(tree_out)

        tree.write(filename, pretty_print=True, xml_declaration=True, encoding="utf-8")