# Funções recursivas e recursividade
 # - funções que podem se chamar de volta
 # - úteis p/ dividir problemas grandes em partes menores
 # Toda função recursiva deve ter:
 # - Um problema que possa ser dividido em partes menores
 # - Um caso recursivo que resolve o pequeno problema
 # - Um caso base que para a recursão
 # - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
 # https://brasilescola.uol.com.br/matematica/fatorial.htm

total = 5
def recursiva(inicio, fim):
    global total
    if inicio == fim:
        return total
    total *= inicio
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva(1, 5))

def factorial (n):
    if n <= 1:
        return 1
    
    return n * factorial (n-1)

