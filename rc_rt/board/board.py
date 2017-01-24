
from .plate.plate import Plate


def print_ninja(bob):
    for y in bob:
        for x in bob[y]:
            print(y, x)


class Board:
    def __init__(self, plates):
        self.working_plates = {}
        self.working_plates.update(plates["NW"].tiles)

        NE = plates["NE"]
        NE.rotate(90)
        NE.offset_coord(x_offset=8)

        SW = plates["SW"]
        SW.rotate(270)
        SW.offset_coord(y_offset=8)

        SE = plates["SE"]
        SE.rotate(180)
        SE.offset_coord(y_offset=8, x_offset=8)

        print_ninja(NE.tiles)
        print_ninja(SW.tiles)
        print_ninja(SE.tiles)

        self.working_plates.update(NE.tiles)
        self.working_plates.update(SW.tiles)
        self.working_plates.update(SE.tiles)

    @staticmethod
    def generate_board(plates_file):
        knwon_plates = []
        for pf in plates_file:
            knwon_plates.append(
                Plate.from_file(pf)
            )
        #  TODO Really Select Plates :p (
        #       NW  NE    1   2
        #       SW  SE    3   4
        # )
        selected_plates = {
            "NW": knwon_plates[0],
            "NE": knwon_plates[1],
            "SW": knwon_plates[2],
            "SE": knwon_plates[2]
        }

        return Board(plates=selected_plates)

    #  TODO
    def generate_objective(self):
        return {
            "x": 1,
            "y": 2
        }

    #  TODO
    def validate(objective, way):
        return True

    #  TODO
    def is_up_authorized(self, x, y):
        return True

    #  TODO
    def is_right_authorized(self, x, y):
        return True

    #  TODO
    def is_left_authorized(self, x, y):
        return True

    #  TODO
    def is_down_authorized(self, x, y):
        return True

    #  TODO
    def where_do_i_stop(self, startx, starty, direction):
        return {
            "x": 5,
            "y": 5
        }
