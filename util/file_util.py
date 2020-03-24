from typing import TextIO


def read_unsigned_byte(file: TextIO) -> int:
    return int.from_bytes(file.read(1), "little")
