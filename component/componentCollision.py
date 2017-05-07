
class ComponentCollision:
    """ ComponentCollision main class """

    aRectangle = {}

    def __init__(self, oRectange, bWall, iEntity):
        self.oRectangle = oRectange
        self.bWall = bWall
        self.iEntity = iEntity
        if bWall == True:
            ComponentCollision.aRectangle[iEntity] = oRectange

    def __del__(self):
        if self.bWall == True:
            del ComponentCollision.aRectangle[self.iEntity]
