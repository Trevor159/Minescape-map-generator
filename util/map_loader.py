from typing import TextIO

from util.file_util import read_unsigned_byte
from util.region import Region, Tile


def load_terrain(region: Region, file: TextIO):
    for z in range(4):
        for x in range(64):
            for y in range(64):
                tile = Tile()
                while True:
                    attribute = read_unsigned_byte(file)

                    if attribute == 0:
                        break
                    elif attribute == 1:
                        height = read_unsigned_byte(file)
                        tile.height = height
                        break
                    elif attribute <= 49:
                        tile.attribute_opcode = attribute
                        tile.overlay_id = read_unsigned_byte(file)
                        tile.overlay_path = (attribute - 2) / 4
                        tile.overlay_rotation = attribute - 2 & 3
                    elif attribute <= 81:
                        tile.settings = attribute - 49
                    else:
                        tile.underlay_id = attribute - 81

                region.tiles[z, x, y] = tile

