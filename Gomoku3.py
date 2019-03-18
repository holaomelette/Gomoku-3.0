#!/usr/bin/python3
#/usr/local/bin/python3
# Set the path to your python3 above

from gtp_connection import GtpConnection
from board_util import GoBoardUtil
from simple_board import SimpleGoBoard

class Gomoku3():
    def __init__(self):
        """
        Gomoku player that selects moves randomly 
        from the set of legal moves.
        Passe/resigns only at the end of game.

        """
        self.name = "GomokuAssignment3"
        self.version = 1.0
        
    def get_move_random(self, board, color):
        return GoBoardUtil.genmove_random(board)
    def get_move_rule(self, board, color):
        return GoBoardUtil.genmove_rule(board)    
    
def run():
    """
    start the gtp connection and wait for commands.
    """
    board = SimpleGoBoard(7)
    con = GtpConnection(Gomoku3(), board)
    con.start_connection()

if __name__=='__main__':
    run()
