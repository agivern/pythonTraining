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
            oImage=pygame.image.load('bluesquare.png'),
            fPositionX = 100,
            fPositionY = 100
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
        ComponentLife(
            iLife = 50
        )
    )
    oWorld.add_component(
        iEntityPlayer,
        ComponentAttack()
    )

    iEntityMonster = oWorld.create_entity()
    oWorld.add_component(
        iEntityMonster,
        ComponentRenderable(
            oImage=pygame.image.load('redsquare.png'),
            fPositionX = 400,
            fPositionY = 250
        )
    )
    oWorld.add_component(
        iEntityMonster,
        ComponentCollision(
            oRectange = Rect(400, 250, 64, 64),
            bWall = True,
            iEntity = iEntityMonster
        )
    )
    oWorld.add_component(
        iEntityMonster,
        ComponentLife(
            iLife = 20
        )
    )

    iEntityMonster = oWorld.create_entity()
    oWorld.add_component(
        iEntityMonster,
        ComponentRenderable(
            oImage=pygame.image.load('redsquare.png'),
            fPositionX = 250,
            fPositionY = 120
        )
    )
    oWorld.add_component(
        iEntityMonster,
        ComponentCollision(
            oRectange = Rect(250, 120, 64, 64),
            bWall = True,
            iEntity = iEntityMonster
        )
    )
    oWorld.add_component(
        iEntityMonster,
        ComponentLife(
            iLife = 30
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
        ProcessorMovement(),
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
        ProcessorTimeManagement (),
        priority = iPriority
    )
    iPriority += 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = -3
                elif event.key == pygame.K_RIGHT:
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = 3
                elif event.key == pygame.K_UP:
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = -3
                elif event.key == pygame.K_DOWN:
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = 3
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    oWorld.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    oWorld.component_for_entity(iEntityPlayer, ComponentAttack).bAttack = True

        oWorld.process()

        oClock.tick(FPS)

if __name__ == "__main__":
    run()
    pygame.quit()
