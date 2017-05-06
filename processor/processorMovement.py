import esper
from component import *
import pygame

class ProcessorMovement(esper.Processor):
    """ ProcessorMovement main class """

    def __init__(self):
        super().__init__()

    def process(self):
        for oEntity, (oComponentVelocity, oComponentRenderable) in self.world.get_components(ComponentVelocity, ComponentRenderable):
            if (self.world.component_for_entity(oEntity, ComponentVelocity).fPositionX != 0
                or self.world.component_for_entity(oEntity, ComponentVelocity).fPositionY != 0) :
                oComponentRenderable.fPositionX += oComponentVelocity.fPositionX
                oComponentRenderable.fPositionY += oComponentVelocity.fPositionY

                # If there a collision rectangle, we move him with the same speed
                if (self.world.has_component(oEntity, ComponentCollision)):
                    self.world.component_for_entity(oEntity, ComponentCollision).oRectangle.move_ip(oComponentVelocity.fPositionX, oComponentVelocity.fPositionY)

