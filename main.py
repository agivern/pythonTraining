#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import esper
import pygame
from pygame.locals import *
from component import *
from processor import *
from model import GameState

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

    iEntityPlayer = oWorld.create_entity(
        ComponentRenderable(
            oImage=pygame.image.load('bluesquare.png')
        ),
        ComponentVelocity(
            fDirectionX = 0,
            fDirectionY = 0
        ),
        ComponentPosition(
            fPositionX = 100,
            fPositionY = 100
        ),
        ComponentLife(
            iLife = 50
        ),
        ComponentAttack(),
        ComponentDirection(),
        ComponentMainCharacter(),
        ComponentCameraTarget()
    )

    oWorld.add_component(
        iEntityPlayer,
        ComponentCollision(
            oRectange = Rect(100, 100, 64, 64),
            bWall = True,
            iEntity = iEntityPlayer
        )
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
        ProcessorTimeManagement(
            oWindow = oWindow
        ),
        priority = iPriority
    )
    iPriority += 1

    oWorld.add_processor(
        ProcessorInput(),
        priority = iPriority
    )
    iPriority += 1

    oGameState = GameState();

    while oGameState.bRunning:
        oWorld.process()

        oClock.tick(FPS)

if __name__ == "__main__":
    run()
    pygame.quit()
