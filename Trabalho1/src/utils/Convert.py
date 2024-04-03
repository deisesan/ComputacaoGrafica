from models import Viewport, Window

class Convert:
    def __init__(self, window: Window, viewport: Viewport):
        self.window = window
        self.viewport = viewport
    
    # Window -> Viewport
    def transform(self, xw, yw):
        xwmin = self.window.xwmin
        xwmax = self.window.xwmax
        ywmin = self.window.ywmin
        ywmax = self.window.ywmax

        xvmin = self.viewport.xvmin
        xvmax = self.viewport.xvmax
        yvmin = self.viewport.yvmin
        yvmax = self.viewport.yvmax


        xv = ((xw - xwmin) / (xwmax - xwmin)) * (xvmax - xvmin)
        yv = (1 - ((yw - ywmin) / (ywmax - ywmin))) * (yvmax - yvmin)
        
        return xv, yv