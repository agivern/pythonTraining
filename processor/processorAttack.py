import esper
from component import *
import pygame
from pygame.locals import *

class ProcessorAttack(esper.Processor):
    """ ProcessorAttack main class """

    def __init__(self):
        super().__init__()

    def process(self):
        for oEntity, (oComponentAttack, oComponentRenderable) in self.world.get_components(ComponentAttack, ComponentRenderable):
            if oComponentAttack.bAttack == True:
                oComponentAttack.bAttack = False

                iEntityAttack = self.world.create_entity()
                self.world.add_component(
                    iEntityAttack,
                    ComponentRenderable(
                        oImage=pygame.image.load('greysquare.png'),
                        fPositionX = oComponentRenderable.fPositionX + oComponentRenderable.fWidth,
                        fPositionY = oComponentRenderable.fPositionY + oComponentRenderable.fHeight / 2
                    )
                )
                self.world.add_component(
                    iEntityAttack,
                    ComponentCollision(
                        oRectange = Rect(
                            oComponentRenderable.fPositionX + oComponentRenderable.fWidth,
                            oComponentRenderable.fPositionY + oComponentRenderable.fHeight / 2,
                            oComponentAttack.fWidth,
                            oComponentAttack.fHeight
                        ),
                        bWall = False,
                        iEntity = iEntityAttack
                    )
                )
                self.world.add_component(
                    iEntityAttack,
                    ComponentFrameLife(
                        iFrame = oComponentAttack.iFrame
                    )
                )
                self.world.add_component(
                    iEntityAttack,
                    ComponentDamage(
                        iDamage = oComponentAttack.iDamage,
                        iEntityProtect = oEntity
                    )
                )
