import curses
import numpy as np
import curses.textpad


board = np.full((3,3),fill_value="_",dtype=str)
line,col = 5,50
moves = {curses.KEY_LEFT:(-2,0),curses.KEY_RIGHT:(2,0),curses.KEY_UP:(0,-1),curses.KEY_DOWN:(0,1)}
chrs = ("x","o")
alias = {32:curses.KEY_RIGHT}


def check_win(ch):

        row = np.any(np.all(board==ch,axis=1)) 
        col = np.any(np.all(board==ch,axis=0))
        dia = np.all(np.diag(board)==ch)
        rdia = np.all(np.diag(np.fliplr(board))==ch)

        win = row or col or dia or rdia

        return win


def check_board(ch):

    ch_win = check_win(ch)

    op = "x" if ch=="o" else "x"

    ch_loss = check_win(op)


    return 1 if ch_win else -1 if ch_loss else 0

def print_board(stdscr):




    l,c = line,col

    for i in range(3):
        for j in range(3):
            stdscr.addstr(l,c,board[i,j])
            c+=2
        l+=1
        c = col

    curses.textpad.rectangle(stdscr, line-1, col-2, line+3, col+6)

    stdscr.refresh()
    stdscr.move(line,col)
    stdscr.refresh()



def main(stdscr):
    
    stdscr.addstr(3,40,f"WELCOME TO TIC-TAC-TOE")
    stdscr.addstr(4,40,"press any key to continue")
    stdscr.getch()
    stdscr.clear()

    print_board(stdscr)


    l,c = line,col
    i,j = 0,0
    game = False

    while(True):

        inp = stdscr.getch() 
        inp = alias[inp] if inp in alias else inp
        let = chr(inp).lower()

        if(inp in moves):

            if game:
                break

            c+=moves[inp][0]
            l+=moves[inp][1] 


            if 0<=c-col<=5 and 0<=l-line<=2:

                stdscr.move(l,c)

            else:
                c-=moves[inp][0]
                l-=moves[inp][1]







        elif(let in chrs):
            if game:
                break

            if board[l-line,abs(col-c)//2] == "_":

                stdscr.addstr(l,c,let)
                stdscr.refresh()
                board[l-line,abs(col-c)//2] = let
            else:
                continue

            check = check_board(let)
            msg = f"{let.upper()} WON!" if check==1 else "DRAW!"

            if check>=0:
                game = True

                stdscr.addstr(3,30+len(msg),f"{msg} PRESS R TO RESTART. PRESS ANYTHING TO END")
                stdscr.refresh()
                l,c = line,col

                continue

        elif let=="r" and game:

            game = False
            board[:] = np.full((3,3),fill_value="_",dtype=str)
            stdscr.clear()
            print_board(stdscr)
            stdscr.refresh()

        elif game:    
            break

        else:
            continue
            
    print("Game over!")



if __name__=="__main__":
    curses.wrapper(main)