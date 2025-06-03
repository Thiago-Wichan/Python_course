# method, @classmethos and @staticmethod

# Sempre que necessitar usar o Self, estamos tratando de um método de instância


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user (self, user): # setter function
        self.user = user

    def set_password (self, password):
        self.password = password

    @classmethod
    def create_with_auth (cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log (x, y):
        return x + y


c1 = Connection.create_with_auth('Ayrton', '1234')

print(c1.user)
print(c1.password)

dict = [
  {
    "name": "Thiago",
    "age": 30
  },
  {
    "name": "Rulian",
    "age": 42
  },
  {
    "name": "Felipo",
    "age": 7
  }
]


c2 = Connection.create_with_auth(dict[0]['name'], dict[0]['age'])

print(c2.user)
print(c2.password)
