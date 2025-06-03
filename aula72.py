texto = 'Almoço'
novo_texto = ''
for bubbles in texto: #interar string - o iterador lhe dará uma unidade por vez
    #print(bubbles) #a primeira variavel "bubbles" é onde "for" irá realizar a iteração

    novo_texto += f'{bubbles}+'

print(novo_texto)