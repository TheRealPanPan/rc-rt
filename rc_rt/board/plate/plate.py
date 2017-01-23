import json


class Plate:
    def __init__(self, tiles):
        self.tiles = tiles

    @staticmethod
    def from_file(filename):
        return Plate(json.load(filename))
