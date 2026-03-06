
def getChessSquareColor(column, row):
    total = column + row
    if column and row in range(1, 9):
        if total % 2 == 0:
            return 'white'
        return 'black'
    return ''


assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
