
from .plate.plate import Plate


class Board:
    def __init__(self, plates):
        self.working_plates = {}
        self.working_plates.update(plates["NW"].tiles)

        NE = plates["NE"]
        NE.rotate(90)
        NE.offset_coord(x_offset=8)
        self._add_to_working_plates(NE.tiles)

        SW = plates["SW"]
        SW.rotate(270)
        SW.offset_coord(y_offset=8)
        self._add_to_working_plates(SW.tiles)

        SE = plates["SE"]
        SE.rotate(180)
        SE.offset_coord(y_offset=8, x_offset=8)
        self._add_to_working_plates(SE.tiles)

    def _add_to_working_plates(self, plates):
        for row in plates:
            if row not in self.working_plates:
                self.working_plates[row] = {}
            self.working_plates[row].update(plates[row])

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
            "SE": knwon_plates[3]
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
