# E X E R C I S E # 2 8 : B O R D E R D R A W I N G

def drawBorder(width, height):
    if width < 2 or height < 2:
        return
    print('+' + (('-')*(width-2)) + '+')
    for x in range(height-2):
        print(('|' + (' ')*(width-2) + '|'), end='\n')
    print('+' + (('-')*(width-2)) + '+')


drawBorder(10, 4)
