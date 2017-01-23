
from .board.board import Board


class RcRt(object):
    def __init__(self, plates_files="../plates"):
        self.board = Board.generate_board(plates_files)

    def get_board(self):
        return self.board
