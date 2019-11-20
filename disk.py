import os
from config import config


class Disk:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, 'r+')

    def close(self):
        self.file.close()

    def get_blocks_count(self):
        with open(self.file_path, 'r') as f:
            return len(f.read()) // config.block_size

    def read(self, block_no):
        """
        Returns data in the block no
        """
        with open(self.file_path, 'r+') as f:
            f.seek(block_no * config.block_size)
            return f.read(config.block_size)

    def write(self, block_no, value):
        """
        Writes data to block
        """
        with open(self.file_path, 'r+') as f:
            f.seek(block_no * config.block_size)
            f.write(value)

    def __str__(self):
        return f'Disk <{self.file_path}> blocks: {self.get_blocks_count()}'

    def __repr__(self):
        return str(self)


class Raid:
    def __init__(self, file_pathes):
        self.disks = [Disk(file_path) for file_path in file_pathes]

    def __str__(self):
        return f'Raid: {self.disks}'

    def close(self):
        for disk in self.disks:
            disk.close()

    def set_block(self, disk_no: int, block_no: int, value: str):
        disk = self.disks[disk_no]
        disk.write(block_no, value)

    def get_block(self, disk_no: int, block_no: int):
        disk = self.disks[disk_no]
        return disk.read(block_no)

    def get_all_blocks(self):
        res = []
        for disk_no, disk in enumerate(self.disks):
            for block_no in range(disk.get_blocks_count()):
                res.append((disk_no, block_no))
        return res