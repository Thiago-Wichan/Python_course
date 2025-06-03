from aula206_b import Person
import json


with open('aula206.json', 'r', encoding='utf8') as file:
    pb = json.load(file)

lt = (pb)
print(lt)

p1 = lt[0]
p1c = Person(**p1)

p1c.id()





