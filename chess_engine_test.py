import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow
from hybrid_algo import *

board = chess.Board()
side = 'White'
engine = ChessEngine()
print(engine.generate_move(board,side))