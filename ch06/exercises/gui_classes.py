class Mario:

    def __init__(self):
        self.grounded = True
        self.coins = 0
        self.pos = (0, 0)


class Terrain:

    def __init__(self):
        self.pos = (0, 0)
        self.touchingPlayer = False
        self.breakable = False


class Enemy:

    def __init__(self):
        self.pos = (0, 0)
        self.movementSpeed = 0
        self.touchingPlayer = False
