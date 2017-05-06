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
    pygame.display.set_caption("Esper Pygame example")
    oClock = pygame.time.Clock()
    pygame.key.set_repeat(1, 1)

    oWorld = esper.World()

    # Add entities in the wolrd
    player = oWorld.create_entity(
        ComponentVelocity(
            fPositionX=0,
            fPositionY=0
        ),
        ComponentRenderable(
            oImage=pygame.image.load("redsquare.png"),
            fPositionX=100,
            fPositionY=100
        )
    )

    enemy = oWorld.create_entity(
        ComponentRenderable(
            oImage=pygame.image.load("bluesquare.png"),
            fPositionX=400,
            fPositionY=250
        )
    )

    # Add processor in the world
    oWorld.add_processor(
        ProcessorRender(
            oWindow = oWindow
        )
    )

    oWorld.add_processor(
        ProcessorMovement(
            fMinX = 0,
            fMaxX = RESOLUTION[0],
            fMinY = 0,
            fMaxY = RESOLUTION[1]
        )
    )

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    oWorld.component_for_entity(player, ComponentVelocity).fPositionX = -3
                elif event.key == pygame.K_RIGHT:
                    oWorld.component_for_entity(player, ComponentVelocity).fPositionX = 3
                elif event.key == pygame.K_UP:
                    oWorld.component_for_entity(player, ComponentVelocity).fPositionY = -3
                elif event.key == pygame.K_DOWN:
                    oWorld.component_for_entity(player, ComponentVelocity).fPositionY = 3
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    oWorld.component_for_entity(player, ComponentVelocity).fPositionX = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    oWorld.component_for_entity(player, ComponentVelocity).fPositionY = 0

        oWorld.process()

        oClock.tick(FPS)

if __name__ == "__main__":
    run()
    pygame.quit()
