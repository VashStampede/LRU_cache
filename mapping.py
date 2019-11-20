import threading
from threading import Lock

from config import config
from random  import shuffle
from str_chunks import chunks_join, chunks_spit

class Mapping:
    def __init__(self, raid):
        self.raid = raid
        self.free_blocks = raid.get_all_blocks()
        shuffle(self.free_blocks)
        self.mappings = {}

        print(f'All blocks: {self.free_blocks}')

    def set_value(self, key: int, value: str):
        chunks = chunks_spit(value, config.block_size)

        if key in self.mappings:
            free_blocks = self.mappings[key]
            self.free_blocks.extend(free_blocks)

        blocks = []
        for chunk in chunks:
            block = self.free_blocks.pop()
            self.raid.set_block(block[0], block[1], chunk)
            blocks.append(block)

        self.mappings[key] = blocks

    def get_value(self, key: int):
        blocks = self.mappings[key]
        chunks = []
        for block in blocks:
            chunk = self.raid.get_block(block[0], block[1])
            chunks.append(chunk)
        return chunks_join(chunks)

