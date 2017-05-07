
class ComponentRenderable:
    """ ComponentRenderable main class """

    def __init__(self, oImage, iDepth=0):
        self.oImage = oImage
        self.iDepth = iDepth
        self.fWidth = oImage.get_width()
        self.fHeight = oImage.get_height()
