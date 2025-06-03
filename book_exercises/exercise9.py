# E X E R C I S E # 9 : C H E S S S Q U A R E C O L O R

def getChessSquareColor(column, row):
    if column and row in range(1, 9):
        if column % 2 == row % 2:
            return 'white'
        else:
            return 'black'
    else:
        return ''


assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
