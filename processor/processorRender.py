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
            fCameraMinX = abs(oComponentPositionCamera.fPositionX)
            fCameraMaxX = fCameraMinX + self.oWindow.get_width()
            fCameraMinY = abs(oComponentPositionCamera.fPositionY)
            fCameraMaxY = fCameraMinY + self.oWindow.get_height()

            # Display the background of the map on the camera screen
            for oEntityMap, oComponentMap in self.world.get_component(ComponentMap):
                for iIndexRow, aRow in enumerate(oComponentMap.aTileMap):
                    fRowMaxY = (iIndexRow + 1) * oComponentMap.iTILESIZE
                    fRowMinY = fRowMaxY - oComponentMap.iTILESIZE
                    # Verify the camera in the axis Y
                    if fRowMaxY > fCameraMinY and fRowMinY < fCameraMaxY:
                        for iIndexColumn, iTileType  in enumerate(aRow):
                            fRowMaxX = (iIndexColumn + 1) * oComponentMap.iTILESIZE
                            fRowMinX = fRowMaxX - oComponentMap.iTILESIZE
                            # Verify the camera in the axis Y
                            if fRowMaxX > fCameraMinX and fRowMinX < fCameraMaxX:
                                pygame.draw.rect(
                                    self.oWindow,
                                    oComponentMap.aColours[iTileType],
                                    (
                                        iIndexColumn*oComponentMap.iTILESIZE - fCameraMinX,
                                        iIndexRow*oComponentMap.iTILESIZE - fCameraMinY,
                                        oComponentMap.iTILESIZE,
                                        oComponentMap.iTILESIZE
                                    )
                                )
                    else:
                        pass

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

