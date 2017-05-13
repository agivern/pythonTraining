
class ComponentItem:
    """ ComponentItem main class """

    def __init__(self, oColor, iPosition):
        self.oColor = oColor
        self.iPosition = iPosition

        iPositionX = iPosition % 5
        iPositionY = iPosition // 5

        # We position the item, *64 to pass previous item,
        # we add 40 pixels to skip the border, and *10 to add 10 pixels between each items
        iPositionX = iPositionX * 64 + 40 + iPositionX * 10
        iPositionY = iPositionY * 64 + 40 + iPositionY * 10

        self.oRectangle = (iPositionX, iPositionY, 64, 64)

