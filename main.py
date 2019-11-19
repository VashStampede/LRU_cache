from random import randint

from config import config
from mapping import Mapping
from disk import Raid


def start_readers(readers_count, mapping):
    for reader in range(readers_count):
        print('Starting reader')
        mapping.get_value(randint(1, 10))

def start_writers(writers_count, mapping):
    for reader in range(writers_count):
        print('Starting writer')
        mapping.set_value(randint(1, 10), 'aaaaaaaaaaa')

def main():
    mapping = Mapping()
    try:
        raid = Raid(config.disk_files)

        disk0 = raid.disks[0]
        disk0.write(3, '33333')
        disk0.write(4, '44444')
        disk0.write(5, '55555')

        print(disk0.read(4))
        print(disk0.read(5))
        disk0.write(4, 'izibr')
        print(disk0.read(3))
        print(disk0.read(4))
        print(disk0.read(5))

        print(raid.disks[0].read(0))
        print(raid)
        start_writers(config.writers_count, mapping)
        start_readers(config.readers_count, mapping)
    finally:
        print('Closing raid')
        raid.close()

if __name__ == '__main__':
    main()