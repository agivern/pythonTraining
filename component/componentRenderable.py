
class ComponentRenderable:
    """ ComponentRenderable main class """

    def __init__(self, oImage, fPositionX, fPositionY, iDepth=0):
        self.oImage = oImage
        self.iDepth = iDepth
        self.fPositionX = fPositionX
        self.fPositionY = fPositionY
        self.fWidth = oImage.get_width()
        self.fHeight = oImage.get_height()
