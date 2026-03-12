import curses
import curses.textpad
import json

N = 4
MAX_DEPTH = 6

line, col = 5, 50

alias = {
    32: curses.KEY_RIGHT,
    97: curses.KEY_LEFT,
    100: curses.KEY_RIGHT,
    119: curses.KEY_UP,
    115: curses.KEY_DOWN
}

move_keys = {
    curses.KEY_LEFT:  (-1,  0),
    curses.KEY_RIGHT: ( 1,  0),
    curses.KEY_UP:    ( 0, -1),
    curses.KEY_DOWN:  ( 0,  1),
}

# ---------- BITBOARD WIN MASKS ----------

WIN_MASKS = []

# rows
for r in range(N):
    mask = 0
    for c in range(N):
        mask |= 1 << (r*N + c)
    WIN_MASKS.append(mask)

# columns
for c in range(N):
    mask = 0
    for r in range(N):
        mask |= 1 << (r*N + c)
    WIN_MASKS.append(mask)

# diagonals
mask = 0
for i in range(N):
    mask |= 1 << (i*N + i)
WIN_MASKS.append(mask)

mask = 0
for i in range(N):
    mask |= 1 << (i*N + (N-1-i))
WIN_MASKS.append(mask)


# ---------- GAME STATE ----------

x_board = 0
o_board = 0
moves = {}


# ---------- SAVE / LOAD ----------

try:
    with open("crazy_progress.json") as f:
        moves = json.load(f)
except:
    moves = {}

for k, v in moves.items():
    r,c = map(int,k.strip("()").split(","))
    idx = r*N+c
    if v=="x":
        x_board |= 1<<idx
    else:
        o_board |= 1<<idx


# ---------- BITBOARD HELPERS ----------

def is_win(board):
    for mask in WIN_MASKS:
        if board & mask == mask:
            return True
    return False


def empty_cells():
    occ = x_board | o_board
    return [i for i in range(N*N) if not occ & (1<<i)]


# ---------- HEURISTIC ----------

def evaluate():

    score = 0

    for mask in WIN_MASKS:

        x = bin(x_board & mask).count("1")
        o = bin(o_board & mask).count("1")

        if x and o:
            continue

        if x:
            score += 10**x

        if o:
            score -= 10**o

    return score


# ---------- MOVE ORDERING ----------

def ordered_moves():

    center = [5,6,9,10]
    corners = [0,3,12,15]

    empties = empty_cells()

    return sorted(
        empties,
        key=lambda m:
            3 if m in center else
            2 if m in corners else
            1,
        reverse=True
    )


# ---------- ALPHA BETA ----------

def alphabeta(depth, alpha, beta, maximizing):

    global x_board, o_board

    if is_win(x_board):
        return 10000-depth

    if is_win(o_board):
        return -10000+depth

    empties = empty_cells()

    if not empties:
        return 0

    if depth==MAX_DEPTH:
        return evaluate()


    if maximizing:

        value = -10**9

        for m in ordered_moves():

            x_board |= 1<<m

            value = max(value,
                        alphabeta(depth+1,alpha,beta,False))

            x_board ^= 1<<m

            alpha = max(alpha,value)

            if alpha>=beta:
                break

        return value

    else:

        value = 10**9

        for m in ordered_moves():

            o_board |= 1<<m

            value = min(value,
                        alphabeta(depth+1,alpha,beta,True))

            o_board ^= 1<<m

            beta = min(beta,value)

            if beta<=alpha:
                break

        return value


# ---------- BEST MOVE ----------

def best_move(player):

    global x_board, o_board

    best_score = -10**9 if player=="x" else 10**9
    best_move = None

    for m in ordered_moves():

        if player=="x":

            x_board |= 1<<m

            score = alphabeta(0,-10**9,10**9,False)

            x_board ^= 1<<m

            if score>best_score:
                best_score=score
                best_move=m

        else:

            o_board |= 1<<m

            score = alphabeta(0,-10**9,10**9,True)

            o_board ^= 1<<m

            if score<best_score:
                best_score=score
                best_move=m

    return best_move


# ---------- CURSES BOARD ----------

def print_board(stdscr):

    occ = {}

    for i in range(N*N):

        if x_board & (1<<i):
            occ[i]="x"
        elif o_board & (1<<i):
            occ[i]="o"
        else:
            occ[i]="_"


    l,c = line,col

    for r in range(N):
        for j in range(N):

            idx=r*N+j
            stdscr.addstr(l,c,occ[idx])
            c+=2

        l+=1
        c=col

    curses.textpad.rectangle(
        stdscr,
        line-1,
        col-2,
        line+N,
        col+N*2
    )

    stdscr.refresh()


# ---------- MAIN ----------

def main(stdscr):

    global x_board,o_board

    stdscr.addstr(3,40,"WELCOME TO TIC TAC TOE")
    stdscr.getch()

    row,colx=0,0
    l,c=line,col

    ori=None

    while ori not in("x","o"):

        stdscr.addstr(4,40,"Choose X or O")
        ori=chr(stdscr.getch()).lower()

    ai="o" if ori=="x" else "x"

    stdscr.clear()
    print_board(stdscr)

    stdscr.move(l,c)

    while True:

        inp=stdscr.getch()

        if inp in alias:
            inp=alias[inp]

        if inp in move_keys:

            dc,dr=move_keys[inp]

            nr=row+dr
            nc=colx+dc

            if 0<=nr<N and 0<=nc<N:

                row,colx=nr,nc

                stdscr.move(
                    line+row,
                    col+colx*2
                )

        elif chr(inp).lower()==ori:

            idx=row*N+colx

            if (x_board|o_board)&(1<<idx):
                continue

            if ori=="x":
                x_board|=1<<idx
            else:
                o_board|=1<<idx

            moves[str((row,colx))]=ori

            print_board(stdscr)

            if is_win(x_board) or is_win(o_board):
                break

            m=best_move(ai)

            if ai=="x":
                x_board|=1<<m
            else:
                o_board|=1<<m

            r=m//N
            c=m%N

            moves[str((r,c))]=ai

            stdscr.clear()
            print_board(stdscr)

            if is_win(x_board) or is_win(o_board):
                break


    stdscr.addstr(line+N+2,col,"Game Over")
    stdscr.getch()

    return moves


if __name__=="__main__":

    var=None

    try:
        var=curses.wrapper(main)

    finally:

        if var is not None:
            with open("crazy_progress.json","w") as f:
                json.dump(var,f)