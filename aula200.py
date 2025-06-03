# Estado das classes:

class Car:
    def __init__(self, name, moving=False):
        self.name = name
        self.moving = moving

    def moviment (self):
        if self.moving:
            return print(f'{self.name} is moving.')
        return print(f'{self.name} is not moving.')
    
    def breaking (self):
        if self.moving:
            self.moving=False
            return print(f'{self.name} is breaking.')
        return print(f'{self.name} is already stopped.')
    
    def acceleration (self):
        if self.moving:
            return print(f'{self.name} is already moving.')
        self.moving=True
        return  print(f'{self.name} is accelerating.')
    
ford = Car('Mustang')

ford.acceleration()
ford.moviment()
ford.breaking()
ford.moviment()

