def add_clients (name, list=None):
    if list is None:
        list=[]
    list.append(name)
    return list

client_1 = add_clients('Otavio')
add_clients('Thiago', client_1)

print(client_1)

client_2 = add_clients('Barbosa')
print(client_2)


