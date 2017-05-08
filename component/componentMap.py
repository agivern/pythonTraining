from component import ComponentCollision
from component import ComponentPosition
from component import ComponentFrameMonsterSpawner
from pygame.locals import Rect


class ComponentMap:
    """ ComponentMap main class """

    iTILESIZE  = 64
    def __init__(self, iMapNumber, oWorld, iEntityMap):
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

        self.aTileAttribute = {
            'color' : {
                DIRT : BROWN,
                GRASS : GREEN,
                WATER : BLUE,
                COAL : BLACK
            },
            'blocked' : {
                WATER : WATER
            }
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

        self.MAPWIDTH  = len(self.aTileMap[0])
        self.MAPHEIGHT = len(self.aTileMap)
        self.iWidth = ComponentMap.iTILESIZE * self.MAPWIDTH
        self.iHeight = ComponentMap.iTILESIZE * self.MAPHEIGHT

        # Check the map to create entities on the wolrd
        for iIndexRow, aRow in enumerate(self.aTileMap):
            for iIndexColumn, iTileType  in enumerate(aRow):
                if iTileType in self.aTileAttribute['blocked']:
                    iEntityBlock = oWorld.create_entity()
                    oWorld.add_component(
                        iEntityBlock,
                        ComponentCollision(
                            oRectange = Rect(
                                iIndexColumn * ComponentMap.iTILESIZE,
                                iIndexRow * ComponentMap.iTILESIZE,
                                ComponentMap.iTILESIZE,
                                ComponentMap.iTILESIZE
                            ),
                            bWall = True,
                            iEntity = iEntityBlock
                        )
                    )
                    oWorld.add_component(
                        iEntityBlock,
                        ComponentPosition(
                            fPositionX = iIndexColumn * ComponentMap.iTILESIZE,
                            fPositionY = iIndexRow * ComponentMap.iTILESIZE
                        )
                    )
                else:
                    pass

        oWorld.create_entity(
            ComponentFrameMonsterSpawner(
                iFrame = 300,
                iEntityMap = iEntityMap
            )
        )
