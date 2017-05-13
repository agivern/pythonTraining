import esper
from component import *
import pygame

class ProcessorRenderInventory(esper.Processor):
    """ ProcessorRenderInventory main class """

    def __init__(self, oWindow, oFont):
        super().__init__()
        self.oWindow = oWindow
        self.oFont = oFont

    def process(self):
        pygame.draw.rect(
            self.oWindow,
            (0,0,0),
            (
                20,
                20,
                self.oWindow.get_width() - 40,
                self.oWindow.get_height() - 40
            )
        )

