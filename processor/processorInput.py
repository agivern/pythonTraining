import esper
from component import *
import processor
import pygame
from pygame.locals import *
from model import GameState

class ProcessorInput(esper.Processor):
    """ ProcessorInput main class """

    def __init__(self, oProcessorList):
        super().__init__()
        self.oProcessorList = oProcessorList


    def process(self):
        oGameState = GameState();

        if oGameState.sState == 'inventory':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    oGameState.bRunning = False

                # Key down
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        oGameState.bRunning = False

                # Key up
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_i:
                        oGameState.sState = 'normal'
                        self.world.remove_processor(processor.ProcessorRenderInventory)

                        self.world.add_processor(
                            self.oProcessorList.aListProcessor['ProcessorMovement'][0],
                            self.oProcessorList.aListProcessor['ProcessorMovement'][1]
                        )
                        self.world.add_processor(
                            self.oProcessorList.aListProcessor['ProcessorCollision'][0],
                            self.oProcessorList.aListProcessor['ProcessorCollision'][1]
                        )
                        self.world.add_processor(
                            self.oProcessorList.aListProcessor['ProcessorAttack'][0],
                            self.oProcessorList.aListProcessor['ProcessorAttack'][1]
                        )
                        self.world.add_processor(
                            self.oProcessorList.aListProcessor['ProcessorTimeManagement'][0],
                            self.oProcessorList.aListProcessor['ProcessorTimeManagement'][1]
                        )

        # Basic command on the game (movement, attack)
        else:
            for iEntityPlayer, oComponentMainCharacter in self.world.get_component(ComponentMainCharacter):

                # Reset the direction of the player
                oPlayerPosition = self.world.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionX = 0
                oPlayerPosition = self.world.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionY = 0

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        oGameState.bRunning = False

                    # Key down
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.world.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = -3
                        elif event.key == pygame.K_d:
                            self.world.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = 3
                        elif event.key == pygame.K_z:
                            self.world.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = -3
                        elif event.key == pygame.K_s:
                            self.world.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = 3
                        elif event.key == pygame.K_ESCAPE:
                            oGameState.bRunning = False


                    # Key up
                    elif event.type == pygame.KEYUP:
                        if event.key in (pygame.K_q, pygame.K_d):
                            self.world.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionX = 0

                        if event.key == pygame.K_i:
                            oGameState.sState = 'inventory'
                            self.world.remove_processor(processor.ProcessorTimeManagement)
                            self.world.remove_processor(processor.ProcessorMovement)
                            self.world.remove_processor(processor.ProcessorAttack)
                            self.world.remove_processor(processor.ProcessorCollision)
                            self.world.add_processor(
                                self.oProcessorList.aListProcessor['ProcessorRenderInventory'][0],
                                self.oProcessorList.aListProcessor['ProcessorRenderInventory'][1]
                            )

                        if event.key in (pygame.K_z, pygame.K_s):
                            self.world.component_for_entity(iEntityPlayer, ComponentVelocity).fDirectionY = 0

                    # Mouse button down
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.world.component_for_entity(iEntityPlayer, ComponentAttack).bAttack = True
                            aMousePosition = pygame.mouse.get_pos()
                            self.world.component_for_entity(iEntityPlayer, ComponentDirection)
                            oPlayerPosition = self.world.component_for_entity(iEntityPlayer, ComponentCollision).oRectangle.center
                            iDistanceX = oPlayerPosition[0] - aMousePosition[0]
                            iDistanceY = oPlayerPosition[1] - aMousePosition[1]

                            # Math to know the direction of the attack (left, right, top, bottom)
                            if abs(iDistanceX) > abs(iDistanceY):
                                if iDistanceX > 0:
                                    oPlayerPosition = self.world.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionX = -1
                                else:
                                    oPlayerPosition = self.world.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionX = 1

                            else:
                                if iDistanceY > 0:
                                    oPlayerPosition = self.world.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionY = -1
                                else:
                                    oPlayerPosition = self.world.component_for_entity(iEntityPlayer, ComponentDirection).iDirectionY = 1

