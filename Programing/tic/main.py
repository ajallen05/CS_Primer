import curses
import numpy as np
import curses.textpad
import json


board = np.full((3, 3), fill_value="_", dtype=str)


moves = {}

try:

    with open("progress.json", "r") as f:
        moves = json.load(f)

except FileNotFoundError:
    pass

except json.JSONDecodeError:
    pass

line, col = 5, 50

move_keys = {
    curses.KEY_LEFT:  (-1,  0),
    curses.KEY_RIGHT: ( 1,  0),
    curses.KEY_UP:    ( 0, -1),
    curses.KEY_DOWN:  ( 0,  1),
}

chrs = ("x", "o")

alias = {
    32: curses.KEY_RIGHT,
    97: curses.KEY_LEFT,
    100: curses.KEY_RIGHT,
    119: curses.KEY_UP,
    115: curses.KEY_DOWN
}


def check_win(ch):
    row = np.any(np.all(board == ch, axis=1))
    col = np.any(np.all(board == ch, axis=0))
    dia = np.all(np.diag(board) == ch)
    rdia = np.all(np.diag(np.fliplr(board)) == ch)
    return row or col or dia or rdia


def minimax(is_maximizing):

    if check_win("x"):
        return 1
    if check_win("o"):
        return -1
    if np.all(board != "_"):
        return 0

    if is_maximizing:

        best = -float("inf")

        for r, c in np.argwhere(board == "_"):

            board[r, c] = "x"
            score = minimax(False)

            board[r, c] = "_"

            if score==1:
                return 1


            best = max(best, score)

        return best

    else:

        best = float("inf")

        for r, c in np.argwhere(board == "_"):

            board[r, c] = "o"
            score = minimax(True)
            board[r, c] = "_"

            if score==-1:
                return -1


            best = min(best, score)

        return best


def best_move(ch):

    available = np.argwhere(board == "_")

    is_maximizing = (ch == "x")

    best_score = -float("inf") if is_maximizing else float("inf")
    best_pos = tuple(available[0])

    for r, c in available:

        board[r, c] = ch
        score = minimax(not is_maximizing)
        board[r, c] = "_"

        if is_maximizing:


            if score==1:
                return (r,c)
            if score > best_score:
                best_score = score
                best_pos = (r, c)

        else:

            if score==-1:
                return (r,c)



            if score < best_score:
                best_score = score
                best_pos = (r, c)

    return best_pos


def check_board(player_ch):

    ch = player_ch.lower()
    op = "x" if ch == "o" else "o"

    if check_win(ch):
        return 1

    if check_win(op):
        return -1

    if np.all(board != "_"):
        return 0

    return None


def print_board(stdscr):

    l, c = line, col

    for i in range(3):
        for j in range(3):
            stdscr.addstr(l, c, board[i, j])
            c += 2
        l += 1
        c = col

    curses.textpad.rectangle(stdscr, line - 1, col - 2, line + 3, col + 6)

    stdscr.refresh()


def main(stdscr):



    for k, v in moves.items():
        r, c = map(int, k.strip("()").split(","))
        board[r, c] = v

    

    print(board)

    stdscr.addstr(3, 40, "WELCOME TO TIC-TAC-TOE")
    stdscr.addstr(4, 40, "press any key to continue")
    stdscr.getch()

    l, c = line, col
    row, colx = 0, 0
    game = False

    stdscr.clear()

    ori = None

    while ori != "x" and ori != "o":

        stdscr.addstr(4, 40, "Choose your character (X or O): ")
        stdscr.clrtoeol()
        stdscr.refresh()

        ori = chr(stdscr.getch()).lower()

    op = "x" if ori == "o" else "o"

    if check_board(ori) is not None:
        board[:] = np.full((3, 3), fill_value="_", dtype=str)

    stdscr.clear()
    print_board(stdscr)

    if ori == "o":

        stdscr.addstr(2, 45, "AI is cookin..")
        stdscr.refresh()

        best = best_move(op)

        board[best] = op
        moves[str((int(best[0]), int(best[1])))] = op

        stdscr.clear()
        print_board(stdscr)

    stdscr.move(l, c)
    stdscr.refresh()

    while True:

        inp = stdscr.getch()

        if inp in alias:
            inp = alias[inp]

        if inp in move_keys:

            if game:
                break

            dc, dr = move_keys[inp]

            new_c = c + dc * 2
            new_l = l + dr

            new_colx = colx + dc
            new_row = row + dr

            if 0 <= new_colx <= 2 and 0 <= new_row <= 2:

                c, l = new_c, new_l
                colx, row = new_colx, new_row

                stdscr.move(l, c)

        elif chr(inp).lower() == ori:

            if game:
                break

            if board[row, colx] != "_":
                continue

            board[row, colx] = ori
            moves[str((row, colx))] = ori

            print_board(stdscr)
            stdscr.refresh()

            check = check_board(ori)

            if check is not None:

                msg = (
                    f"{ori.upper()} WON!"
                    if check == 1
                    else "DRAW!"
                    if check == 0
                    else f"{op.upper()} WON!"
                )

                game = True

                stdscr.addstr(
                    2,
                    40,
                    f"{msg} PRESS R TO RESTART. PRESS ANYTHING TO END"
                )

                stdscr.move(l, c)
                stdscr.refresh()
                continue

            stdscr.addstr(2, 45, "AI is cookin..")
            stdscr.refresh()

            best = best_move(op)

            board[best] = op
            moves[str((int(best[0]), int(best[1])))] = op

            stdscr.clear()
            print_board(stdscr)

            stdscr.refresh()

            check = check_board(ori)

            if check is not None:

                msg = (
                    f"{ori.upper()} WON!"
                    if check == 1
                    else "DRAW!"
                    if check == 0
                    else f"{op.upper()} WON!"
                )

                game = True

                stdscr.addstr(
                    2,
                    40,
                    f"{msg} PRESS R TO RESTART. PRESS ANYTHING TO END"
                )

            stdscr.move(l, c)
            stdscr.refresh()

        elif chr(inp).lower() == "r" and game:

            game = False
            board[:] = "_"
            moves.clear()

            row, colx = 0, 0
            l, c = line, col

            stdscr.clear()
            print_board(stdscr)

            if ori == "o":

                stdscr.addstr(2, 45, "AI is cookin..")
                stdscr.refresh()

                best = best_move(op)

                board[best] = op
                moves[str((int(best[0]), int(best[1])))] = op

                stdscr.clear()
                print_board(stdscr)

            stdscr.move(l, c)
            stdscr.refresh()

        elif game:
            break

    stdscr.addstr(line + 5, col - 2, "Game over! Press any key to exit.")
    stdscr.refresh()

    stdscr.getch()
    stdscr.clear()

    return moves


if __name__ == "__main__":


    with open("progress.json", "w") as f:




        var = moves

        try:
            curses.wrapper(main)

        except:
            
            

            if var is not None:

                if np.all(board != "_"):
                    json.dump({},f)

                else:
                    json.dump(var, f)

        else:

            with open("progress.json", "w") as f:
                json.dump({}, f)
