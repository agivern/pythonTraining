import esper
from component import *
import pygame

class ProcessorCollision(esper.Processor):
    """ ProcessorMovement main class """

    def __init__(self):
        super().__init__()

    def process(self):
        for oEntity, oComponentCollision in self.world.get_component(ComponentCollision):

            # Verify the collision only for entities with a velocity
            if (self.world.has_component(oEntity, ComponentVelocity)):
                oComponentVelocity = self.world.component_for_entity(oEntity, ComponentVelocity)

                # Verify the velocity speed, only an entity with a movement
                # can collide
                if (oComponentVelocity.fPositionX != 0
                    or oComponentVelocity.fPositionY != 0) :
                    oComponentCollision.oRectangle.move_ip(oComponentVelocity.fPositionX, oComponentVelocity.fPositionY)
                    aIndexCollision = oComponentCollision.oRectangle.collidelistall(oComponentCollision.aRectangle)

                    # We verify if the collision rectangle of the entity collide
                    # with an other rectangle than himself
                    if (len(aIndexCollision) > 1):
                        oComponentCollision.oRectangle.move_ip(-oComponentVelocity.fPositionX, -oComponentVelocity.fPositionY)
                        oComponentVelocity.fPositionX = 0
                        oComponentVelocity.fPositionY = 0
                    else:
                        oComponentCollision.oRectangle.move_ip(-oComponentVelocity.fPositionX, -oComponentVelocity.fPositionY)
