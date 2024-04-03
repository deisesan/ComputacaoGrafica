from models import Dot, Window, Viewport

class Convert:
    # Window -> Viewport
    def transform(self, dot: Dot, window: Window, viewport: Viewport):
        xw, yw = dot

        xwmin = window.xwmin
        xwmax = window.xwmax
        ywmin = window.ywmin
        ywmax = window.ywmax

        xvmin = viewport.xvmin
        xvmax = viewport.xvmax
        yvmin = viewport.yvmin
        yvmax = viewport.yvmax


        xv = ((xw - xwmin) / (xwmax - xwmin)) * (xvmax - xvmin)
        yv = (1 - ((yw - ywmin) / (ywmax - ywmin))) * (yvmax - yvmin)
        
        return xv, yv