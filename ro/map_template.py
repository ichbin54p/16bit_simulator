class Map:
    class blocks:
        class Dirt:
            def __init__(self, x, y, state):
                self.x = x
                self.y = y
                self.state = state
                self.img = "/textures/dirt.png"
                self.id = 0
    class Entities:
        pass