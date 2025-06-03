import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def id (self):
        return print(self.name, self.age)
    

p1 = Person('Thiago', 30)
p2 = Person('Rulian', 42)
p3 = Person('Felipo', 7)
lt = [vars(p1), vars(p2), p3.__dict__]


with open ('aula206.json', 'w', encoding='utf8') as file:
    json.dump(
        lt,
        file,
        indent=2
    )





