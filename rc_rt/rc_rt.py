from glob import glob
from rc_rt.board.board import Board


class RcRt(object):
    def __init__(self, plates_file_glob="../plates/plate_*.json"):
        self.board = Board.generate_board(glob(plates_file_glob))

    def get_board(self):
        return self.board


if __name__ == "__main__":
    print(RcRt().get_board())
