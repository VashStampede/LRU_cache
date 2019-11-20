from random import randint, choice
from time import sleep

from config import config
from dictionary import get_random_quote
from mapping import Mapping
from disk import Raid
from threading import Thread, Lock

from rwlock import RWLock

mutex = Lock()
rwlock = RWLock()

def reader_loop(mapping, reader_no):
    while True:
        with rwlock.r_locked():
            mutex.acquire()
            key = randint(1, 10)
            try:
                val = mapping.get_value(key)
                print(f'Reader {reader_no}: {val}')
                sleep(1)
            except KeyError:
                print(f'Reader {reader_no}: Key {key} not found')

def writer_loop(mapping, writer_no):
    while True:
        with rwlock.w_locked():
            mutex.acquire()
            key = randint(1, 10)
            val = get_random_quote()
            mapping.set_value(key, val)
            print(f'Wrote {writer_no}: {val}')
            sleep(1)


def start_readers(readers_count, mapping):
    for reader_no in range(readers_count):
        print('Starting reader')
        r = Thread(target=reader_loop, args=(mapping, reader_no))
        r.start()


def start_writers(writers_count, mapping):
    for writer_no in range(writers_count):
        print('Starting writer')
        w = Thread(target=writer_loop, args=(mapping, writer_no))
        w.start()




def main():

    try:
        raid = Raid(config.disk_files)
        mapping = Mapping(raid)
        print(raid.disks[0].read(0))
        print(raid)
        start_writers(config.writers_count, mapping)
        start_readers(config.readers_count, mapping)
    finally:
        print('Closing raid')
        raid.close()


if __name__ == '__main__':
    main()
