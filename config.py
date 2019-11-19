
class Config:
    def __init__(self, config_file='config.txt'):
        with open(config_file, 'r') as f:
            config = f.readlines()

        self.block_size = int(config[0])
        self.cache_size = int(config[1])
        self.readers_count = int(config[2])
        self.writers_count = int(config[3])
        self.disk_files = [f.strip() for f in config[4:]]

    def __str__(self):
        return f'''
            block size: {self.block_size},
            cache size: {self.cache_size},
            readers: {self.readers_count},
            writers: {self.writers_count},
            disks: {self.disk_files}
        '''

config = Config()
