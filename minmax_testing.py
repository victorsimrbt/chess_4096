from minmax import *
import time

tree = MinMaxTree()
board = chess.Board()

start = time.time()
move,effectiveness = tree.predict(board,'White',depth = 3)
end = time.time()

print(end-start)
print(move)