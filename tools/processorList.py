from processor import *

def singleton(cls):
    instance = None
    def ctor(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance
    return ctor

@singleton
class ProcessorList:
    def __init__(self):
        self.aListProcessor = {}

    def initProcessor(self, oWindow, oFont):
        oProcessorRender = ProcessorRender(
            oWindow = oWindow,
            oFont = oFont
        )

        oProcessorMovement = ProcessorMovement(
            oWindow = oWindow
        )

        oProcessorTimeManagement = ProcessorTimeManagement(
            oWindow = oWindow
        )

        iPriority = 0
        self.aListProcessor['ProcessorRender'] = (oProcessorRender, iPriority)
        iPriority += 1
        self.aListProcessor['ProcessorMovement'] = (oProcessorMovement, iPriority)
        iPriority += 1
        self.aListProcessor['ProcessorCollision'] = (ProcessorCollision(), iPriority)
        iPriority += 1
        self.aListProcessor['ProcessorAttack'] = (ProcessorAttack(), iPriority)
        iPriority += 1
        self.aListProcessor['ProcessorTimeManagement'] = (oProcessorTimeManagement, iPriority)
        iPriority += 1
        self.aListProcessor['ProcessorInput'] = (ProcessorInput(oProcessorList = self), iPriority)

