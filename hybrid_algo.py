from neural_network import *  
from minmax import *

class ChessEngine():
    
    def __init__(self,algorithms = [MinMaxTree,NeuralNetwork]):
        self.algorithms = algorithms
    
    def generate_move(self,board,side):
        moves = []
        effe = []
        for algo in self.algorithms:
            move,effectiveness = algo().predict(board,side)
            moves.append(move)
            effe.append(effectiveness)
        moves = np.array(moves)
        effe = np.array(effe)
        
        idx = np.argmax(effe)
        
        print('Algorithm Used:',self.algorithms[idx].__name__)
        print(effe)
        return moves[np.argmax(effe)]
            

        