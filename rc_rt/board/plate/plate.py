import json


class PlateRotationException(Exception):
    pass


def _shift_urdl_right(tile):
    urdl = tile["urdl"]
    tile["urdl"] = int(urdl / 10)
    if urdl % 2 != 0:
        #  Was ending by 1 so adding 1000 to reinsert the lost 1
        tile["urdl"] = 1000 + tile["urdl"]


class Plate:
    def __init__(self, tiles):
        self.raw_tiles = tiles
        self.current_tiles = tiles

    def reset_original_tiles(self):
        self.current_tiles = self.raw_tiles

    @staticmethod
    def from_file(filename):
        with open(filename, mode='r') as f:
            return Plate(json.load(f))

    @property
    def tiles(self):
        return self.current_tiles

    def __rotate(self, deg):
        temp_tiles = {}
        while deg > 0:
            for y in self.current_tiles:
                for x in self.current_tiles[y]:
                    n_y = x
                    n_x = str(9 - int(y))  # Such math, such wow
                    if n_y not in temp_tiles:
                        temp_tiles[n_y] = {}

                    temp_tiles[n_y][n_x] = self.current_tiles[y][x]
                    temp_tiles[n_y][n_x]["coord"]["x"] = n_x
                    temp_tiles[n_y][n_x]["coord"]["y"] = n_y

                    _shift_urdl_right(temp_tiles[n_y][n_x])

            deg = deg - 90
            self.current_tiles = temp_tiles
            temp_tiles = {}

    def rotate(self, deg):
        if deg not in [0, 90, 180, 270, -90, -180, -270]:
            raise PlateRotationException("Can't rotate at < %s > deg" % deg)

            if deg < 0:
                deg = 360 + deg  # Transform left rotation to right one.

        self.__rotate(deg)

    def offset_coord(self, y_offset=0, x_offset=0):
        et = {}
        for y in self.current_tiles:
            n_y = str(int(y) + y_offset)
            for x in self.current_tiles[y]:
                n_x = str(int(x) + x_offset)
                if n_y not in et:
                    et[n_y] = {}
                et[n_y][n_x] = self.current_tiles[y][x]
                et[n_y][n_x]["coord"]["x"] = n_x
                et[n_y][n_x]["coord"]["y"] = n_y

        self.current_tiles = et
