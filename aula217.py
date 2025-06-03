# Composição

class Client:
    def __init__ (self, name):
        self.name = name
        self.address = []

    def to_list_adress (self):
        for address in self.address:
            print(address.street, address.number)

    def to_insert_adress (self, street, number):
        self.address.append(Address(street, number))

class Address:
    def __init__ (self, street, number):
        self.street = street
        self.number = number

client1 = Client('Thiago')
client1.to_insert_adress('Rua Magnólia', 137)

client1.to_list_adress()

