import os
import re

from amulet.world_interface import load_world

from util.color_util import block_from_tile, process_tile
from util.file_util import handle_files
from util.map_loader import load_terrain
from util.mc_util import set_block, initialize_world
from util.region import Region

if __name__ == "__main__":
    empty_world_path = "resources/emptymap"
    # WARNING ANY DIRECTORY AT THE OUTPUT PATH WILL BE DELETED
    output_world_path = "output/testworld1"

    handle_files(empty_world_path, output_world_path)
    world = load_world(output_world_path)
    initialize_world(world)
    # set_block(world, 0, 64, 0)
    # world.save()
    path = "rscachedump/tiledata"
    regions = []
    pattern = re.compile("m(\d+)_(\d+).dat")
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'rb') as f:
            match = pattern.match(filename)
            regionX = match.group(1)
            regionY = match.group(2)
            region = Region(int(regionX), int(regionY))
            load_terrain(region, f)
            regions.append(region)
            f.close()

    for region in regions:
        for z in range(len(region.tiles)):
            for x in range(len(region.tiles[z])):
                for y in range(len(region.tiles[z][x])):
                    tile = region.tiles[z][x][y]
                    process_tile(world, z, x, y, regions, region)

    world.save()
