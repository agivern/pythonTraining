
class ComponentCollision:
    """ ComponentRenderable main class """

    aRectangle = []

    def __init__(self, oRectange):
        self.oRectangle = oRectange
        ComponentCollision.aRectangle.append(oRectange)
