from config import config


class Mapping:
    def __init__(self):
        self.free_blocks = []
        self.mappings = {}

    def set_value(self, key: int, value: str):
        self.mappings[key] = value

    def get_value(self, key):
        return self.mappings[key]
