# Operadres de atribuição

# =  +=  -=  *=  **=  /= //= %=
# 
# Usando o comando Continue para pular alguma repetição no while


contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 30:
        print('Não há o número', contador, 'nesta lista')
        continue

    print(contador)

    if contador == 50:
        break
