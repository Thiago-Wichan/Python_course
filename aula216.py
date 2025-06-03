# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
import json

class Cart:
    def __init__(self):
        self.product = []

    def total(self):
        return sum([p.price for p in self.product])

    def insert_products (self, *product):
        for products in product:
            self.product.append(products)

    def list_products(self):
        print()
        for products in self.product:
            print(products.name, products.price)
        print()
        

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
p1, p2 = Product('Camisa', 15.0), Product('Cerveja', 35.0)
cart.insert_products(p1, p2)
cart.list_products()
print(f'Your cart costs {cart.total()}.')



# class Carrinho:
#     def __init__(self):
#         self._produtos = []

#     def total(self):
#         return sum([p.preco for p in self._produtos])

#     def inserir_produtos(self, *produtos):
#         # self._produtos.extend(produtos)
#         # self._produtos += produtos
#         for produto in produtos:
#             self._produtos.append(produto)

#     def listar_produtos(self):
#         print()
#         for produto in self._produtos:
#             print(produto.nome, produto.preco)
#         print()


# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco


# carrinho = Carrinho()
# p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
# carrinho.inserir_produtos(p1, p2)
# carrinho.listar_produtos()
# print(carrinho.total())