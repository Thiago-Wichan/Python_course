def my_repr (self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name} - ({class_dict})'
    return class_repr


def add_repr (cls):
    cls.__repr__ = my_repr
    return cls


def my_team (method):
    def intern (self, *args, **kwargs):
        result = method (self, *args, **kwargs)
        if 'Flamengo' in result:
            return f'Seu time é o maior do mundo'
        return result
    return intern


@add_repr
class Team:
    def __init__(self, name):
        self.name = name

    @my_team
    def name_speak(self):
        return f'Your team is {self.name}'


def my_plane (method):
    def intern (self, *args, **kwargs):
        result = method (self, *args, **kwargs)
        if 'Airbus' in result:
            return f'Your airplane is a Airbus, congratulations!'
        return result
    return intern


@add_repr
class Airplane:
    def __init__(self, name):
        self.name = name
    @my_plane
    def name_speak(self):
        return f'Your airplane is {self.name}'

airbus = Airplane('Airbus')
flamengo = Team('Flamengo')

print(flamengo)
print(airbus)

print(flamengo.name_speak())
print(airbus.name_speak())
