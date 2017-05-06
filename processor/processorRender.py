import esper
from component import *
import pygame

class ProcessorRender(esper.Processor):
    """ ProcessorRender main class """

    def __init__(self, oWindow, clear_color=(0, 0, 0)):
        super().__init__()
        self.oWindow = oWindow
        self.clear_color = clear_color

    def process(self):
        self.oWindow.fill(self.clear_color)

        for oEntity, oComponentRenderable in self.world.get_component(ComponentRenderable):
            self.oWindow.blit(
                oComponentRenderable.oImage,
                (
                    oComponentRenderable.fPositionX,
                    oComponentRenderable.fPositionY
                )
            )

        pygame.display.flip()

