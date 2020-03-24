import glob
import os
import json
import shutil
from distutils.dir_util import copy_tree
from amulet import Block
from amulet.api.chunk import Chunk
from amulet.api.errors import ChunkDoesNotExist
from amulet.utils import block_coords_to_chunk_coords
from amulet.world_interface import load_world
from amulet.api.world import World

from util.color_util import block_from_tile


def set_block(world: World, x: int, y: int, z: int, block: str):
    if not (0 <= y <= 255):
        raise IndexError("The supplied Y coordinate must be between 0 and 255")

    cx, cz = block_coords_to_chunk_coords(x, z);

    try:
        chunk = world.get_chunk(cx, cz)
    except ChunkDoesNotExist:
        world.put_chunk(Chunk(cx, cz))
        chunk = world.get_chunk(cx, cz)

    offset_x, offset_z = x - 16 * cx, z - 16 * cz
    chunk.blocks[offset_x, y, offset_z] = world.palette.get_add_block(Block(namespace="universal_minecraft", base_name=block))
    # print("set block x: " + str(x) + " y: " + str(y) + " z: " + str(z) + " to block " + block)
    chunk.changed = True


def handle_files(empty_world_path: str, output_world_path: str):
    if os.path.exists(output_world_path):
        shutil.rmtree(output_world_path)
    os.makedirs(output_world_path)
    copy_tree(empty_world_path, output_world_path)


if __name__ == "__main__":
    empty_world_path = "resources/emptymap"
    # WARNING ANY DIRECTORY AT THE OUTPUT PATH WILL BE DELETED
    output_world_path = "output/testworld1"

    handle_files(empty_world_path, output_world_path)
    world = load_world(output_world_path)
    # set_block(world, 0, 64, 0)
    # world.save()
    path = "rscachedump/tiledata"
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f:
            data = json.loads(f.read())
            baseX = data["regionX"] << 6
            baseY = data["regionY"] << 6
            regionID = data["regionX"] << 8 | data["regionY"]
            print(data["regionX"])
            print(data["regionY"])
            print(baseX)
            print(baseY)
            print(regionID)
            for z in range(len(data["tiles"])):
                for x in range(len(data["tiles"][z])):
                    for y in range(len(data["tiles"][z][x])):
                        tiledata = data["tiles"][z][x][y]
                        block = block_from_tile(tiledata["underlayId"], tiledata["overlayId"])
                        print(block)
                        if block is not None:
                            # -y to make the cardinal directions the same as RS
                            set_block(world, x, 64 + z*5, -y, block)
            f.close()

    world.save()
