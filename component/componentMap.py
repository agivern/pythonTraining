
class ComponentMap:
    """ ComponentMap main class """

    iTILESIZE  = 64
    def __init__(self, iMapNumber):
        self.iMapNumber = iMapNumber

        BLACK = (0, 0, 0)
        BROWN = (153, 76, 0)
        GREEN = (0, 255, 0)
        BLUE  = (0, 0, 255)

        DIRT  = 0
        GRASS = 1
        WATER = 2
        COAL  = 3

        self.aColours =   {
            DIRT : BROWN,
            GRASS : GREEN,
            WATER : BLUE,
            COAL : BLACK
        }

        self.aTileMap = [
            [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER],
            [WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER]
        ]

        #useful game dimensions
        self.MAPWIDTH  = len(self.aTileMap[0])
        self.MAPHEIGHT = len(self.aTileMap)
        self.iWidth = ComponentMap.iTILESIZE * self.MAPWIDTH
        self.iHeight = ComponentMap.iTILESIZE * self.MAPHEIGHT
