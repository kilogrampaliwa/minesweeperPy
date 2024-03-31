import random as RD


class board():

    def __init__(self, x, y, bombs_quantity):
        """
        1) Creates board of x, y size.
        2) Puts bombs in random places.
        3) Creates board with bombs and proper digits.
        """
        self._bombs_quantity = bombs_quantity
        if isinstance(x, int) and isinstance(y, int):
            self._drawBoard(x, y, bombs_quantity)
        else:
            print("Wrong x y inputs.")
            input()

    def _probability(self, left_bombs, left_fields):
        "Returns probability from left board size and left empty fields"
        return float(left_bombs / left_fields)

    def _draw(self, probability):
        "Gives random True-Falaw with given probability"

        probability = round(probability*1000)
        probArray = []

        true_n = 0
        false_n = 0

        for i in range(probability):
            true_n+=1
        for i in range(1000-probability):
            false_n+=1

        for i in range(1000):
            import math
            if math.floor(i/2)==0 and true_n>0:
                probArray.append(True)
                true_n-=1
            elif false_n>0:
                probArray.append(False)
                false_n-=1
            else:probArray.append(True)

        rando = RD.randrange(0, 1000)
        return (probArray[rando])

    def _drawBoard(self, x, y, bombs_quantity):
        "Gives board with bomb and digitsset"
        self._setBombs(x, y, bombs_quantity)
        self._setDigits()

    def _setBombs(self, x, y, bombs_quantity):
        "Gives board with bomb set"

        emptyFields = x*y
        bombs_left = bombs_quantity

        self._board = []

        for m in range(y):
            linia = []
            for n in range(x):

                probab = self._probability(bombs_left, emptyFields)
                result = self._draw(probab)
                if result: bombs_left-=1
                emptyFields-=1

                linia.append(result)
            self._board.append(linia)

    def _setDigits(self):
        "Gives board with digits set"

        y = len(self._board)
        x = len(self._board[0])

        boardDigits = []

        for m in range(y):
            digitLine = []
            for n in range(x):

                bombsFound = 0

                if self._board[m][n]:
                    bombsFound='*'
                else:
                    if m-1>=0:

                        if n-1>=0:

                            if self._board[m-1][n-1]: bombsFound+=1

                        if self._board[m-1][n]    : bombsFound+=1

                        if n+1<x:

                            if self._board[m-1][n+1] : bombsFound+=1

                    if m+1<y:

                        if n-1>=0:

                            if self._board[m+1][n-1]: bombsFound+=1

                        if self._board[m+1][n]    : bombsFound+=1

                        if n+1<x:

                            if self._board[m+1][n+1] : bombsFound+=1

                    if n-1>=0:
                        if self._board[m][n-1]: bombsFound+=1
                    if n+1<x:
                        if self._board[m][n+1] : bombsFound+=1

                digitLine+=str(bombsFound)
            boardDigits.append(digitLine)
        self._board = boardDigits

    def giveBoard(self):
        return self._board

    def printBoard(self):

        line0 = "+--"
        for n in range(len(self._board[0])*2):
            line0+='-'
        line0+='+'
        print(line0)
        for y in self._board:
            line = ''
            line += "| "
            for x in y:
                if x == '0': line +="  "
                else: line +=' '+x
            line+= " |"
            print(line)
        print(line0)



