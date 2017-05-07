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
        for oEntityCamera, (oComponentPositionCamera, oComponentCamera) in self.world.get_components(ComponentPosition, ComponentCamera):
            self.oWindow.get_width() / 2
            self.oWindow.get_height() / 2
            for oEntity, (oComponentRenderable, oComponentPosition) in self.world.get_components(ComponentRenderable, ComponentPosition):
                self.oWindow.blit(
                    oComponentRenderable.oImage,
                    (
                        oComponentPosition.fPositionX,
                        oComponentPosition.fPositionY
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
                            oComponentPosition.fPositionX,
                            oComponentPosition.fPositionY
                        )
                    )

        pygame.display.flip()

