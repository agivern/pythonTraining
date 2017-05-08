#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import esper
import pygame
from pygame.locals import *
from component import *
from processor import *

FPS = 60
RESOLUTION = 720, 480

def run():
    pygame.init()
    oWindow = pygame.display.set_mode(RESOLUTION)
    pygame.display.set_caption('Drinkor')
    oFont = pygame.font.SysFont("monospace", 15)

    oClock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)

    oWorld = esper.World()

    # Add entities in the wolrd
    iEntityMap = oWorld.create_entity()
    oWorld.add_component(
        iEntityMap,
        ComponentMap(
            iMapNumber = 1,
            oWorld = oWorld,
            iEntityMap = iEntityMap
        )
    )

    iEntityCamera = oWorld.create_entity(
        ComponentVelocity(
            fDirectionX = 0,
            fDirectionY = 0
        ),
        ComponentPosition(
            fPositionX = 0,
            fPositionY = 0
        ),
        ComponentCamera()
    )

    iEntityPlayer = oWorld.create_entity()
    oWorld.add_component(
        iEntityPlayer,
        ComponentCollision(
            oRectange = Rect(100, 100, 64, 64),
            bWall = True,
            iEntity = iEntityPlayer
        )
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentRenderable(
            oImage=pygame.image.load('bluesquare.png')
        ),
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentVelocity(
            fDirectionX = 0,
            fDirectionY = 0
        )
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentPosition(
            fPositionX = 100,
            fPositionY = 100
        )
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentLife(
            iLife = 50
        )
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentAttack()
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentDirection(),
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentMainCharacter(),
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentCameraTarget(),
    )

    # Add processor in the world
    iPriority = 0

    oWorld.add_processor(
        ProcessorRender(
            oWindow = oWindow,
            oFont = oFont
        ),
        priority = iPriority
    )
    iPriority += 1

    oWorld.add_processor(
        ProcessorMovement(
            oWindow = oWindow,
            iEntityCamera = iEntityCamera,
            iEntityMap = iEntityMap
        ),
        priority = iPriority
    )
    iPriority += 1

    oWorld.add_processor(
        ProcessorCollision(),
        priority = iPriority
    )
    iPriority += 1

    oWorld.add_processor(
        ProcessorAttack(),
        priority = iPriority
    )
    iPriority += 1

    oWorld.add_processor(
        ProcessorTimeManagement (
            oWindow = oWindow
        ),
        priority = iPriority
    )
    iPriority += 1

    running = True
    while running:
        oPlayerPosition = oWorld.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionX = 0
        oPlayerPosition = oWorld.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionY = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = -3
                elif event.key == pygame.K_d:
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = 3
                elif event.key == pygame.K_z:
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = -3
                elif event.key == pygame.K_s:
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = 3
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_q, pygame.K_d):
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = 0
                if event.key in (pygame.K_z, pygame.K_s):
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    oWorld.component_for_entity(iEntityPlayer, ComponentAttack).bAttack = True
                    aMousePosition = pygame.mouse.get_pos()
                    oWorld.component_for_entity(iEntityPlayer, ComponentDirection)
                    oPlayerPosition = oWorld.component_for_entity(iEntityPlayer, ComponentCollision).oRectangle.center
                    iDistanceX = oPlayerPosition[0] - aMousePosition[0]
                    iDistanceY = oPlayerPosition[1] - aMousePosition[1]
                    if abs(iDistanceX) > abs(iDistanceY):
                        if iDistanceX > 0:
                            oPlayerPosition = oWorld.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionX = -1
                        else:
                            oPlayerPosition = oWorld.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionX = 1
                    else:
                        if iDistanceY > 0:
                            oPlayerPosition = oWorld.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionY = -1
                        else:
                            oPlayerPosition = oWorld.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionY = 1


        oWorld.process()

        oClock.tick(FPS)

if __name__ == "__main__":
    run()
    pygame.quit()
