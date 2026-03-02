# E X E R C I S E # 2 7 : R E C T A N G L E D R A W I N G

def drawRectangle(width, height):
    i = 0
    if width < 1 or height < 1:
        return ''
    while i < height:
        print('#'*width)
        i += 1


drawRectangle(10, 0)
