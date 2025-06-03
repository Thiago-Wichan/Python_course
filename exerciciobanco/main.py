""" Main """

from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, number: int):
        self.agency = agency
        self.number = number
        self._balance = 0.0

    def __repr__(self):
        represent_ = (f'Type - {self.__class__.__name__}\n'
                      f'Agency - {self.agency}\n'
                      f'Number - {self.number}\n')
        return represent_

    @abstractmethod
    def withdraw(self, value: float):
        self.value = value

    def balance(self):
        return print(f'Your balance is ${self._balance:.2f}.\n\r')

    def deposit(self, value: float):
        self.value = value
        self._balance += self.value
        print(f'You have depositted ${value:.2f}')
        return self.balance()


class Current(Account):
    def withdraw(self, value: float):
        self.value = value
        special_balance = self._balance + 500
        if special_balance < self.value:
            print('You do not have enought balance.\r')
            return self.balance()
        self._balance -= self.value
        print(f'You have withdrawn ${value:.2f}')
        return self.balance()


class Saving(Account):
    def withdraw(self, value: float):
        if self._balance < value:
            print('You do not have enought balance.\r')
            return self.balance()
        self._balance -= value
        print(f'You have withdrawn ${value:.2f}')
        return self.balance()


class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        return f'{self._name}'


class Client(Person):
    def __init__(self, name):
        self._name = name

    def make_account(self, account):
        self.agency = account.agency
        self.number = account.number


class Bank(Client, Account):
    def __init__(self, name: str, client, account):
        self.name = name
        self.client = client
        self.account = account

    def validate(self):
        valid_agency_number = range(1000)

        if self.client.agency not in valid_agency_number or\
           self.client.number not in valid_agency_number:
            print('Agency or number is not valid.')
            return False

        if self.client.agency != self.account.agency:
            print('Client does not have an account.')
            return False

        if self.client.number != self.account.number:
            print('This number of account is incorrect.')
            return False

        print(
            f'Bank - {self.name}\n'
            f'Client - {self.client.name}\n'
            f'{self.account}'
        )
        return True

    def withdraw(self, value: float):
        if self.validate():
            self.account.withdraw(value=value)
            return self.account.balance
        return self._balance

    def deposit(self, value: float):
        if self.validate():
            self.account.deposit(value)
            return self.account.balance
        return self._balance


a1 = Current(agency=500, number=120)
p1 = Person('Tobias', 20)
c1 = Client(p1)
c1.make_account(a1)
b1 = Bank('Itaú', c1, a1)
b1.withdraw(100)
b1.deposit(340)
b1.withdraw(400)


a2 = Saving(700, 328)
p2 = Person('Thiago', 30)
c2 = Client(p2)
c2.make_account(a2)
b2 = Bank('Caixa', c2, a2)
b2.deposit(5000)
b2.withdraw(5200)
