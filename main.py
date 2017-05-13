#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import esper
import pygame
from pygame.locals import *
from component import *
from processor import *
from model import GameState
from tools import ProcessorList

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
    oProcessorList = ProcessorList()
    oProcessorList.initProcessor(
        oWindow = oWindow,
        oFont = oFont
    )

    oWorld.add_processor(
        oProcessorList.aListProcessor['ProcessorRender'][0],
        oProcessorList.aListProcessor['ProcessorRender'][1]
    )
    oWorld.add_processor(
        oProcessorList.aListProcessor['ProcessorMovement'][0],
        oProcessorList.aListProcessor['ProcessorMovement'][1]
    )
    oWorld.add_processor(
        oProcessorList.aListProcessor['ProcessorCollision'][0],
        oProcessorList.aListProcessor['ProcessorCollision'][1]
    )
    oWorld.add_processor(
        oProcessorList.aListProcessor['ProcessorAttack'][0],
        oProcessorList.aListProcessor['ProcessorAttack'][1]
    )
    oWorld.add_processor(
        oProcessorList.aListProcessor['ProcessorTimeManagement'][0],
        oProcessorList.aListProcessor['ProcessorTimeManagement'][1]
    )
    oWorld.add_processor(
        oProcessorList.aListProcessor['ProcessorInput'][0],
        oProcessorList.aListProcessor['ProcessorInput'][1]
    )

    oGameState = GameState();

    while oGameState.bRunning:

        oWorld.process()
        pygame.display.flip()

        oClock.tick(FPS)

if __name__ == "__main__":
    run()
    pygame.quit()
