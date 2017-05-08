import esper
from component import *
import pygame
from pygame.locals import *
from random import randrange

class ProcessorTimeManagement(esper.Processor):
    """ ProcessorTimeManagement main class """

    def __init__(self, oWindow):
        super().__init__()
        self.oWindow = oWindow

    def process(self):
        for oEntity, oComponentFameLife in self.world.get_component(ComponentFrameLife):
            oComponentFameLife.iFrame -= 1
            if oComponentFameLife.iFrame <= 0:
                self.world.delete_entity(oEntity)

        for oEntityCamera, (oComponentPositionCamera, oComponentCamera) in self.world.get_components(ComponentPosition, ComponentCamera):
            fCameraMinX = abs(oComponentPositionCamera.fPositionX)
            fCameraMaxX = fCameraMinX + self.oWindow.get_width()
            fCameraMinY = abs(oComponentPositionCamera.fPositionY)
            fCameraMaxY = fCameraMinY + self.oWindow.get_height()

            # Spawn monster each time it's necessary
            for oEntity, oComponentFrameMonsterSpawner in self.world.get_component(ComponentFrameMonsterSpawner):
                oComponentFrameMonsterSpawner.iCurentFrame -= 1
                if oComponentFrameMonsterSpawner.iCurentFrame <= 0:
                    oComponentFrameMonsterSpawner.iCurentFrame = oComponentFrameMonsterSpawner.iFrame

                    oComponentMap = self.world.component_for_entity(oComponentFrameMonsterSpawner.iEntityMap, ComponentMap)
                    iPositionX = randrange(oComponentMap.iWidth)
                    iPositionY = randrange(oComponentMap.iHeight)

                    # Monster can't spawn inside the camera screen
                    # We delete him immediatly if he collides something
                    if ((iPositionY < fCameraMinY - 64 or iPositionY > fCameraMaxY)
                        or (iPositionX < fCameraMinX - 64 or iPositionX > fCameraMaxX)):
                        iEntityMonster = self.world.create_entity()
                        self.world.add_component(
                            iEntityMonster,
                            ComponentRenderable(
                                oImage=pygame.image.load('redsquare.png')
                            )
                        )
                        self.world.add_component(
                            iEntityMonster,
                            ComponentCollision(
                                oRectange = Rect(
                                    iPositionX - fCameraMinX,
                                    iPositionY - fCameraMinY,
                                    64,
                                    64
                                ),
                                bWall = True,
                                iEntity = iEntityMonster
                            )
                        )
                        self.world.add_component(
                            iEntityMonster,
                            ComponentPosition(
                                fPositionX = iPositionX - fCameraMinX,
                                fPositionY = iPositionY - fCameraMinY
                            )
                        )
                        self.world.add_component(
                            iEntityMonster,
                            ComponentLife(
                                iLife = 20
                            )
                        )

                        oComponentCollision = self.world.component_for_entity(iEntityMonster, ComponentCollision)
                        aIndexCollision = oComponentCollision.oRectangle.collidedictall(oComponentCollision.aRectangle,1)

                        for i, (iEntity, oRectangle) in enumerate(aIndexCollision):
                            if iEntityMonster != iEntity:
                                self.world.delete_entity(iEntityMonster)
                                break
                    else:
                        pass
                else:
                    pass
