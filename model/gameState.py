
def singleton(cls):
    instance = None
    def ctor(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance
    return ctor

@singleton
class GameState:
    def __init__(self):
        self.bRunning = True
