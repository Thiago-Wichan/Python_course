# LETRA QUE APARECEU MAIS VEZES #

frase = 'eu voce todos nos '.lower()

i = 0
qtd_mais_vezes = 0
letra_mais_repetida = ''

while i < len(frase):
    letra = frase[i]
    qtd_mais_vezes_atual = frase.count(letra)

    if letra == ' ':
        i += 1
        continue

    if qtd_mais_vezes < qtd_mais_vezes_atual:
        qtd_mais_vezes = qtd_mais_vezes_atual
        letra_mais_repetida = letra
    

    i += 1

    
print(f'A letra que apareceu mais vezes foi "{letra_mais_repetida}" que apareceu {qtd_mais_vezes}x')




   

