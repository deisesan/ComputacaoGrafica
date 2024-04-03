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

        xvpmin = self.viewport.xvpmin
        xvpmax = self.viewport.xvpmax
        yvpmin = self.viewport.yvpmin
        yvpmax = self.viewport.yvpmax

        xvp = ((xw - xwmin) / (xwmax - xwmin)) * (xvpmax - xvpmin)
        yvp = (1 - ((yw - ywmin) / (ywmax - ywmin))) * (yvpmax - yvpmin)
        
        return xvp, yvp