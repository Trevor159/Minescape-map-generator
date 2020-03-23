import glob
import os

# from amulet.world_interface.formats import Format
from amulet.world_interface.formats.anvil.anvil_format import AnvilFormat
from amulet.api.world import World

if __name__ == "__main__":

    world = World("output", AnvilFormat(None))
    # path = "resources/tiledata"
    # for filename in os.listdir(path):
    #     with open(os.path.join(path, filename), 'r') as f:
    #         print(filename)
    #         f.close()
