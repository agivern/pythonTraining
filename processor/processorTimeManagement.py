import esper
from component import *

class ProcessorTimeManagement(esper.Processor):
    """ ProcessorTimeManagement main class """

    def __init__(self):
        super().__init__()

    def process(self):
        for oEntity, oComponentFameLife in self.world.get_component(ComponentFrameLife):
            oComponentFameLife.iFrame -= 1
            if oComponentFameLife.iFrame <= 0:
                self.world.delete_entity(oEntity)
