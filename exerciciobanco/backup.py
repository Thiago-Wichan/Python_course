""" Main """

from abc import ABC

class Account(ABC):
    def __init__(self, agency, number):
        self.agency = agency
        self.number = number
        self._balance = 0

    def __repr__(self):
        represent_ =   (f'Type - {self.__class__.__name__}\n'
                        f'Agency - {self.agency}\n'
                        f'Number - {self.number}\n')
        return represent_

    def withdraw(self, value: int | float):
        self.value = value
        if self._balance < self.value:
            print('You do not have enought balance.\n\r')
            return self._balance        
        self._balance -= self.value
        return self._balance
    
    def deposit(self, value: int | float):
        self.value = value
        self._balance += self.value
        return self._balance

    def balance(self):
        raise NotImplementedError ('Others classes needs to implement this.')
       
class Current(Account):
    """Current accounts has 500 dolars in extra balance"""
    @property    
    def balance(self):
        self._balance += 500
        return print(f'Your balance is ${self._balance}.')

class Saving(Account):
    @property
    def balance(self):
        return print(f'Your balance is ${self._balance}.')


class Person(ABC):
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
    
    def get_name(self):
        return f'{self._name}'
    def get_age(self):
        return self._age
    def __repr__(self):
        return f'{self._name}'
    
class Client(Person):
    def __init__(self, name: str):
        self._name = name
                
    def make_account(self, account):
        self.agency = account.agency
        self.number = account.number
    

class Bank(Client, Current, Saving):
    def __init__(self, name, client, account):
        self.name = name
        self.client = client
        self.account = account
        self._balance = self.account._balance
    

    def validate(self):
            valid_agency_number = range(1000)

            if self.client.agency not in valid_agency_number or\
            self.client.number not in valid_agency_number:
                return print('Agency or number is not valid.')
            
            if self.client.agency != self.account.agency:
                return print('This client does not have an account.')
            
            if self.client.number != self.account.number:
                return print('This number of account is incorrect.')

            print (
                f'Client - {self.client.get_name()}\n'
                f'Bank - {self.name}\n'
                f'Agency - {self.client.agency}\n'
                f'Number - {self.client.number}\n'
                f'Balance - {self.account._balance}'
            )

    def withdraw(self, value):
        self.validate()
        super().withdraw(value=value)
        return super().balance
    
    def deposit(self, value):
        self.validate()
        super().deposit(value)
        return super().balance
        
a1 = Saving(agency= 500, number= 120)
c1 = Person('Tobias', 20)

c1 = Client(c1)
c1.make_account(a1)

b1 = Bank('Itaú', c1, a1)
b1.deposit(100)
b1.withdraw(100)








# c2 = Saving(500, 100)

# c2.deposit(100)
# print(c2.balance)
# c2.withdraw(50)
# print(c2.balance)