import esper
from component import *
import pygame

class ProcessorCollision(esper.Processor):
    """ ProcessorMovement main class """

    def __init__(self):
        super().__init__()

    def process(self):
        # Verify the collision only for entities with a velocity
        for oEntity, (oComponentCollision, oComponentVelocity) in self.world.get_components(ComponentCollision, ComponentVelocity):
            if oComponentCollision.bWall == True:
                # Verify the velocity speed, only an entity with a movement
                # can collide
                if (oComponentVelocity.fDirectionX != 0
                    or oComponentVelocity.fDirectionY != 0) :
                    oComponentCollision.oRectangle.move_ip(oComponentVelocity.fDirectionX, oComponentVelocity.fDirectionY)
                    aIndexCollision = oComponentCollision.oRectangle.collidedictall(oComponentCollision.aRectangle,1)

                    # We verify if the collision rectangle of the entity collide
                    # with an other rectangle than himself
                    for i, (iEntity, oRectangle) in enumerate(aIndexCollision):
                        if oEntity != iEntity:
                            oComponentVelocity.fDirectionX = 0
                            oComponentVelocity.fDirectionY = 0
                        else:
                            oComponentCollision.oRectangle.move_ip(-oComponentVelocity.fDirectionX, -oComponentVelocity.fDirectionY)

        # Verify the collision with a attack
        for oEntity, (oComponentCollision, oComponentDamage) in self.world.get_components(ComponentCollision, ComponentDamage):
            aIndexCollision = oComponentCollision.oRectangle.collidedictall(oComponentCollision.aRectangle,1)
            for i, (iEntity, oRectangle) in enumerate(aIndexCollision):
                # Verify if the collision it's with himself or a protected entity
                if (oComponentDamage.iEntityProtect != iEntity
                    and oEntity != iEntity):
                    # Verify if the entity collide has life
                    if self.world.has_component(iEntity, ComponentLife):
                        oComponentLife = self.world.component_for_entity(iEntity, ComponentLife)
                        oComponentLife.iLife -= oComponentDamage.iDamage
                        self.world.delete_entity(oEntity)
                        if oComponentLife.iLife <= 0:
                            self.world.delete_entity(iEntity)
