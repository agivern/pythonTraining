import esper
from component import *
import pygame

class ProcessorMovement(esper.Processor):
    """ ProcessorMovement main class """

    def __init__(self):
        super().__init__()

    def process(self):
        for oEntity, (oComponentVelocity, oComponentRenderable) in self.world.get_components(ComponentVelocity, ComponentRenderable):
            if (oComponentVelocity.fDirectionX != 0
                or oComponentVelocity.fDirectionY != 0) :
                oComponentRenderable.fPositionX += oComponentVelocity.fDirectionX
                oComponentRenderable.fPositionY += oComponentVelocity.fDirectionY

                # If there a collision rectangle, we move him with the same speed
                if self.world.has_component(oEntity, ComponentCollision):
                    self.world.component_for_entity(oEntity, ComponentCollision).oRectangle.move_ip(oComponentVelocity.fDirectionX, oComponentVelocity.fDirectionY)

