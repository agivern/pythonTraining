import esper
from component import *
import pygame

class ProcessorRender(esper.Processor):
    """ ProcessorRender main class """

    def __init__(self, oWindow, oFont, clear_color=(0, 0, 0)):
        super().__init__()
        self.oWindow = oWindow
        self.oFont = oFont
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

            if self.world.has_component(oEntity, ComponentCollision):
                pygame.draw.rect(
                    self.oWindow,
                    (150,150,150),
                    self.world.component_for_entity(oEntity, ComponentCollision).oRectangle
                )

            if self.world.has_component(oEntity, ComponentLife):
                label = self.oFont.render(
                    str(self.world.component_for_entity(oEntity, ComponentLife).iLife),
                    1,
                    (0,0,0)
                )
                self.oWindow.blit(label,
                    (
                        oComponentRenderable.fPositionX,
                        oComponentRenderable.fPositionY
                    )
                )

        pygame.display.flip()

