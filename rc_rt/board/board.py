
from .plate.plate import Plate


class Board:
    def __init__(self, plates):
        self.plates = plates

        #  Prepare plates (rotate + expand)

    @staticmethod
    def generate_board(plates_file):
        knwon_plates = []
        for pf in plates_file:
            knwon_plates.append(
                Plate.from_file(pf)
            )
        #  TODO Select plates
        selected_plates = []

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
