import esper
from component import *
import pygame

class ProcessorMovement(esper.Processor):
    """ ProcessorMovement main class """

    def __init__(self, fMinX, fMaxX, fMinY, fMaxY):
        super().__init__()
        self.fMinX = fMinX
        self.fMaxX = fMaxX
        self.fMinY = fMinY
        self.fMaxY = fMaxY

    def process(self):
        for oEntity, (oComponentVelocity, oComponentRenderable) in self.world.get_components(ComponentVelocity, ComponentRenderable):
            oComponentRenderable.fPositionX += oComponentVelocity.fPositionX
            oComponentRenderable.fPositionY += oComponentVelocity.fPositionY

            oComponentRenderable.fPositionX = max(self.fMinX, oComponentRenderable.fPositionX)
            oComponentRenderable.fPositionY = max(self.fMinY, oComponentRenderable.fPositionY)
            oComponentRenderable.fPositionX = min(self.fMaxX - oComponentRenderable.fWidth, oComponentRenderable.fPositionX)
            oComponentRenderable.fPositionY = min(self.fMaxY - oComponentRenderable.fHeight, oComponentRenderable.fPositionY)
