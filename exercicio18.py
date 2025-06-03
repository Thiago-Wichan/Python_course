class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None 
        self._company = None

    @property
    def engine (self):
        return self._engine
    
    @engine.setter
    def engine (self, value):
        self._engine = value

    @property
    def company (self):
        return self._company
    
    @company.setter
    def company (self, value):
        self._company = value


class Engine:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, name):
        self.name = name
        
gol = Car('Gol')
volkswagen = Company('Volkswagen')
ap = Engine('AP 1.6')

gol.company = volkswagen
gol.engine = ap

print(gol.name, gol.company.name, gol.engine.name)

palio = Car('Palio')
fiat = Company('Fiat')
fire = Engine('Fire 1.0')

palio.company = fiat
palio.engine = fire

print(palio.name, palio.company.name, palio.engine.name)

voyage = Car('Voyage')
voyage.company = volkswagen
voyage.engine = ap

print(voyage.name, voyage.company.name, voyage.engine.name)



