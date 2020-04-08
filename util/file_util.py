import os
import shutil
from distutils.dir_util import copy_tree
from typing import TextIO

def handle_files(empty_world_path: str, output_world_path: str):
    if os.path.exists(output_world_path):
        shutil.rmtree(output_world_path)
    os.makedirs(output_world_path)
    copy_tree(empty_world_path, output_world_path)

def read_unsigned_byte(file: TextIO) -> int:
    return int.from_bytes(file.read(1), "little")
