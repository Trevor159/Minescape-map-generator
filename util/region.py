import numpy

class Region:
    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y
        self.tiles = numpy.empty((4, 64, 64), dtype=Tile)



class Tile:
    def __init__(self):
        self.height = None
        self.settings = 0
        self.overlay_id = 0
        self.overlay_path = 0
        self.overlay_rotation = 0
        self.underlay_id = 0
        self.attribute_opcode = 0

