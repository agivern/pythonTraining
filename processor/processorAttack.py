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

                iAttackerDirectionX = self.world.component_for_entity(oEntity, ComponentDirection).iDirectionX
                iAttackerDirectionY = self.world.component_for_entity(oEntity, ComponentDirection).iDirectionY

                fAttackPositionX = oComponentRenderable.fPositionX + oComponentRenderable.fWidth / 2
                fAttackPositionY = oComponentRenderable.fPositionY + oComponentRenderable.fHeight / 2


                if iAttackerDirectionX == -1:
                    fAttackPositionX -= oComponentRenderable.fWidth / 2 + oComponentAttack.fWidth
                    fWidth = oComponentAttack.fWidth
                    fHeight = oComponentAttack.fHeight
                elif iAttackerDirectionX == 1:
                    fAttackPositionX += oComponentRenderable.fWidth / 2
                    fWidth = oComponentAttack.fWidth
                    fHeight = oComponentAttack.fHeight
                else:
                    pass

                if iAttackerDirectionY == -1:
                    fAttackPositionY -= oComponentRenderable.fHeight / 2 + oComponentRenderable.fHeight
                    fWidth = oComponentAttack.fHeight
                    fHeight = oComponentAttack.fWidth
                elif iAttackerDirectionY == 1:
                    fAttackPositionY += oComponentRenderable.fHeight / 2
                    fWidth = oComponentAttack.fHeight
                    fHeight = oComponentAttack.fWidth
                else:
                    pass

                iEntityAttack = self.world.create_entity()
                self.world.add_component(
                    iEntityAttack,
                    ComponentRenderable(
                        oImage=pygame.image.load('greysquare.png'),
                        fPositionX = fAttackPositionX,
                        fPositionY = fAttackPositionY
                    )
                )
                self.world.add_component(
                    iEntityAttack,
                    ComponentCollision(
                        oRectange = Rect(
                            fAttackPositionX,
                            fAttackPositionY,
                            fWidth,
                            fHeight
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

                if oComponentAttack.fVelocity != 0:
                    fDirectionX = oComponentAttack.fVelocity * self.world.component_for_entity(oEntity, ComponentDirection).iDirectionX
                    fDirectionY = oComponentAttack.fVelocity * self.world.component_for_entity(oEntity, ComponentDirection).iDirectionY

                    self.world.add_component(
                        iEntityAttack,
                        ComponentVelocity(
                            fDirectionX = fDirectionX,
                            fDirectionY = fDirectionY
                        )
                    )
