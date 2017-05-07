import esper
from component import *
import pygame

class ProcessorMovement(esper.Processor):
    """ ProcessorMovement main class """

    def __init__(self, oWindow, iEntityCamera, iEntityMap):
        super().__init__()
        self.oWindow = oWindow
        self.iEntityCamera = iEntityCamera
        self.iEntityMap = iEntityMap

    def process(self):
        fCameraDirectionX = self.world.component_for_entity(self.iEntityCamera, ComponentVelocity).fDirectionX = 0
        fCameraDirectionY = self.world.component_for_entity(self.iEntityCamera, ComponentVelocity).fDirectionY = 0
        fCameraPositionX = abs(self.world.component_for_entity(self.iEntityCamera, ComponentPosition).fPositionX)
        fCameraPositionY = abs(self.world.component_for_entity(self.iEntityCamera, ComponentPosition).fPositionY)
        fMapWidth = self.world.component_for_entity(self.iEntityMap, ComponentMap).iWidth
        fMapHeight = self.world.component_for_entity(self.iEntityMap, ComponentMap).iHeight
        for oEntity, (oComponentVelocity, oComponentPosition, oComponentCameraTarget) in self.world.get_components(ComponentVelocity, ComponentPosition, ComponentMainCharacter):
            if oComponentVelocity.fDirectionX != 0:
                if (fCameraPositionX <= (fMapWidth - self.oWindow.get_width())
                    and oComponentVelocity.fDirectionX > 0
                    and oComponentPosition.fPositionX > (self.oWindow.get_width() / 2)):
                    fCameraDirectionX = oComponentVelocity.fDirectionX
                elif (fCameraPositionX > 0
                    and oComponentVelocity.fDirectionX < 0
                    and oComponentPosition.fPositionX < (self.oWindow.get_width() / 2)):
                    fCameraDirectionX = oComponentVelocity.fDirectionX

            if oComponentVelocity.fDirectionY != 0:
                if (fCameraPositionY > 0
                    and oComponentVelocity.fDirectionY < 0
                    and oComponentPosition.fPositionY < (fMapHeight - self.oWindow.get_height())):
                        fCameraDirectionY = oComponentVelocity.fDirectionY
                elif (fCameraPositionY <= (fMapHeight - self.oWindow.get_height())
                    and oComponentVelocity.fDirectionY > 0
                    and oComponentPosition.fPositionY > (self.oWindow.get_height() / 2)):
                        fCameraDirectionY = oComponentVelocity.fDirectionY

        if (fCameraDirectionX != 0 or fCameraDirectionY != 0):
            for oEntity, oComponentPosition in self.world.get_component(ComponentPosition):
                if (fCameraDirectionX != 0 or fCameraDirectionY != 0) :
                    oComponentPosition.fPositionX -= fCameraDirectionX
                    oComponentPosition.fPositionY -= fCameraDirectionY
                    # If there a collision rectangle, we move him with the same speed
                    if self.world.has_component(oEntity, ComponentCollision):
                        self.world.component_for_entity(oEntity, ComponentCollision).oRectangle.move_ip(-fCameraDirectionX, -fCameraDirectionY)


        for oEntity, (oComponentVelocity, oComponentPosition) in self.world.get_components(ComponentVelocity, ComponentPosition):
            fDirectionX = oComponentVelocity.fDirectionX
            fDirectionY = oComponentVelocity.fDirectionY
            if (fDirectionX != 0 or fDirectionY != 0) :
                oComponentPosition.fPositionX += fDirectionX
                oComponentPosition.fPositionY += fDirectionY
                # If there a collision rectangle, we move him with the same speed
                if self.world.has_component(oEntity, ComponentCollision):
                    self.world.component_for_entity(oEntity, ComponentCollision).oRectangle.move_ip(fDirectionX, fDirectionY)
