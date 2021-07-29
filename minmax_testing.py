from minmax import *
import time

tree = MinMaxTree()
board = chess.Board()

board.push_san('e4')
board.push_san('e5')
board.push_san('f4')

start = time.time()
move,effectiveness = tree.predict(board,'Black',depth = 3)
end = time.time()

utilities = np.array([node.utility for node in tree.nodes[0]])
print(utilities)

print(end-start)
print(move)