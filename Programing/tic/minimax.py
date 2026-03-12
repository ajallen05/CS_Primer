import numpy as np

temp = np.full((3,3),fill_value="_",dtype=str)


def minimax(chr):

    val = check_board(chr)

    if check_board(temp)<2:
        return val
    

def all_moves():

    return np.argwhere(board=="_")

    


def best_move(ch):

    moves = all_moves()

    best = -1 * np.inf

    for i,j in moves:

        board[i,j] = ch
        score = minimax(chr)
        board[i,j] = "_"

        if(score==1):
            return (i,j)
        else:

            best = max(best,score)

    return (i,j)




    


        