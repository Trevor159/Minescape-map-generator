import glob
import os
from distutils.dir_util import copy_tree
from amulet import Block
from amulet.api.chunk import Chunk
from amulet.api.errors import ChunkDoesNotExist
from amulet.utils import block_coords_to_chunk_coords
from amulet.world_interface import load_world
from amulet.api.world import World

def set_block(world: World, x: int, y: int, z: int):
    if not (0 <= y <= 255):
        raise IndexError("The supplied Y coordinate must be between 0 and 255")

    cx, cz = block_coords_to_chunk_coords(x, z);

    try:
        chunk = world.get_chunk(cx, cz)
    except ChunkDoesNotExist:
        world.put_chunk(Chunk(cx, cz))
        chunk = world.get_chunk(cx, cz)

    offset_x, offset_z = x - 16 * cx, z - 16 * cz
    chunk.blocks[offset_x, y, offset_z] = world.palette.get_add_block(Block(namespace="universal_minecraft", base_name="diamond_block"))
    chunk.changed = True


def handle_files(empty_world_path: str, output_world_path: str):
    if os.path.exists(output_world_path):
        os.rmdir(output_world_path)
    os.mkdir(output_world_path)
    copy_tree(empty_world_path, output_world_path)


if __name__ == "__main__":
    empty_world_path = "resources/emptymap"
    # WARNING ANY DIRECTORY AT THE OUTPUT PATH WILL BE DELETED
    output_world_path = "output/testworld1"

    handle_files(empty_world_path, output_world_path)
    world = load_world(output_world_path)
    try:
        cx, cz = block_coords_to_chunk_coords(0, 0);
        chunk = world.get_chunk(cx, cz)
        block = world.get_block(0, 64, 0)
        print(block.base_name)
    except ChunkDoesNotExist:
        print("no chunk")
    set_block(world, 0, 64, 0)
    block = world.get_block(0, 64, 0)
    print(block.base_name)
    world.save()
    # path = "resources/tiledata"
    # for filename in os.listdir(path):
    #     with open(os.path.join(path, filename), 'r') as f:
    #         print(filename)
    #         f.close()
