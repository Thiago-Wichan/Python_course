class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __repr__ (self):
        return f'Point: ({self.x!r}, {self.y!r})'

    def __add__ (self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point (new_x, new_y)
    
p1 = Point (2, 5)
p2 = Point (5, 2)

p3 = p1 + p2

print (p3)