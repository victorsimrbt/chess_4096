from board_conversion import *
import chess
from keras.models import load_model
from time import sleep
from IPython.display import display, HTML, clear_output

print('HELLO')
model = load_model("chess_model")
        
board = chess.Board()

def display_board(board, use_svg):
    if use_svg:
        return board._repr_svg_()
    else:
        return "<pre>" + str(board) + "</pre>"

for i in range(100):
    translated = translate_board(board)

    move_matrix = model.predict(translated.reshape(1,8,8,12))[0][0]
    move_matrix = filter_legal_moves(board,move_matrix)

    move= np.unravel_index(np.argmax(move_matrix, axis=None), move_matrix.shape)
    move = chess.Move(move[0],move[1])
    board.push(move)

    html = display_board(board, True)
    clear_output(wait=True)
    display(HTML(html))
    sleep(4.0)
    
    if board.is_game_over():
        break