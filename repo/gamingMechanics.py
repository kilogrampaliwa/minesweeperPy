

class gamingField():
    """ Contains two tables:
        - background table
        - front table"""
    
    def __init__(self, createdField):
        "Saves background field and creates front field"

        self.__backgroundField = createdField
        self.__y = len(createdField)
        self.__x = len(createdField[0])

        self.__frontField = []
        for j in range(self.__y):
            line = []
            for i in range(self.__x):
                line.append(chr(176))
            self.__frontField.append(line)

    def __check(self, x, y):
        "Check field of given coordinates"

#self.__backgroundField[y][x]

        def ifNumber(xi, yi):
            if self.__backgroundField[yi][xi] in ['1','2','3','4','5','6','7','8','9']:
                self.__frontField[yi][xi] = self.__backgroundField[yi][xi]
                return (True, self.__backgroundField[yi][xi])
            elif self.__backgroundField[yi][xi] == '0':
                if self.__frontField[yi][xi] == '&':
                    self.__frontField[yi][xi] = '$'
                elif self.__frontField[yi][xi] == '$' or self.__frontField[yi][xi] == ' ':
                    self.__frontField[yi][xi] == ' '
                else:
                    self.__frontField[yi][xi] = '&'
                return (False, self.__backgroundField[yi][xi])
            else: return (False, self.__backgroundField[yi][xi])

        def ifZero(i, j):

                self.__frontField[j][i] = ' '

                if j-1>=0:

                    if i-1>=0:  ifNumber(i-1, j-1)

                    ifNumber(i, j-1)

                    if i+1<self.__x:    ifNumber(i+1, j-1)


                if j+1<self.__y:

                    if i-1>=0:  ifNumber(i-1, j+1)

                    ifNumber(i, j+1)

                    if i+1<self.__x:    ifNumber(i+1, j+1)


                if i-1>=0:
                    ifNumber(i-1, j)

                if i+1<self.__x:
                    ifNumber(i+1, j)

        if ifNumber(x, y)[0]:
            return ifNumber(x, y)[1]
        else:
            if self.__backgroundField[y][x] == '*':
                self.__frontField = self.__backgroundField
                for j in self.__frontField:
                    for i in j:
                        if i=='0': i=' '
                return self.__backgroundField[y][x]

            elif self.__backgroundField[y][x] == '0':
                ifZero(x, y)


        areAnds = True

        while areAnds:
            areAnds = False
            for j in range(self.__y):
                if '&' in self.__frontField[j] or '$' in self.__frontField[j]:
                    areAnds=True
                for i in range(self.__x):
                    if self.__frontField[j][i] == '&' or self.__frontField[j][i] == '$':
                        ifZero(i, j)


    def giveFields(self):
        "Gives fields"

        return (self.__frontField, self.__backgroundField)

    def giveCheckedFields(self, x, y):
        "Checkes and gives fields."

        self.__check(int(x), int(y))

        self.giveFields()


import fieldCreation

podstawa = fieldCreation.board(60, 32, 200)
stol = gamingField(podstawa.giveBoard())

def printer(stolik):
    pole = stol.giveFields()
    obraz = []
    for y in range(len(pole[0])):
        linia = ""
        for x in range(len(pole[0][0])):
            linia+=(pole[0][y][x])
        linia+=("          ")
        for x in range(len(pole[1][0])):
            linia+=(pole[1][y][x])
        obraz.append(linia)

    for linia in obraz:
        print(linia)

while True:
    printer(stol)
    print("Give x and y:")
    x = input(" x =  ")
    y = input(" y =  ")
    stol.giveCheckedFields(x, y)