import os

win_conditions = (

    {0,1,2},{3,4,5},{6,7,8}, # Horizontal

    {0,3,6},{1,4,7},{2,5,8}, # Vertical

    {0,4,8},{2,4,6}  # Diagonal
)

symbols = ("X","O","DRAW")


class Game:
    def __init__(self):

        self.moves = []
        self.board = list("abcdefghi")

    def __str__(self):
        return "\n---+---+---\n".join("  |".join(self.board[i:i+3]) for i in [0, 3, 6])


    def add_moves(self,m):
        try:
            assert len(m)==1
            mi = ord(m.lower()) - ord("a")           
            assert mi not in self.moves
            assert 0<=mi<9
        except (TypeError,AssertionError):
            return False
        self.board[mi] = symbols[(len(self.moves))%2]

        self.moves.append(mi)

        return True
    
    def check_win(self):
        for i,m in enumerate((set(self.moves[::2]),set(self.moves[1::2]))):
            for c in win_conditions:
                if(len(c-m)==0):
                    return i  
        if len(self.moves)==9:
            return -1 # Draw
        
        return None # game not over

def main():
    g = Game()
    print(g)
    is_win = None

    while(True):

        is_win = g.check_win()
        if is_win is not None:
            out = symbols[is_win]+" WON" if is_win>=0 else symbols[is_win]
            print(out)
            break

        a = input("Enter your Move: ")
        while(g.add_moves(a) != True):
            a = input("Enter a Valid Move: ")

        os.system("cls")
        print(g)


if __name__ == "__main__":
    main()






    







