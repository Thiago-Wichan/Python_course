lista = ['Pedra', 'Papel', 'Tesoura']

import random

contador_jogador = 0
contador_maquina = 0

def confronto(x):

    global contador_jogador
    global contador_maquina

    jogada_jogador = lista[int_jogada]
    jogada_maquina = random.randint(0,2)

    print()
    print(
            f'A sua jogada é {jogada_jogador}\n'
            f'A jogada da máquina é {lista[jogada_maquina]}'
        )
    
    print()

    empate = 'Empate.'
    derrota = 'Máquina venceu!'
    vitoria = 'Você venceu!'
    
    if int_jogada == jogada_maquina:
        return print(empate)

    if int_jogada == 0:
        if jogada_maquina == 1:
            contador_maquina += 1
            return print(derrota)
        elif jogada_maquina == 2:
            contador_jogador += 1
            return print(vitoria)

    if int_jogada == 1:
        if jogada_maquina == 0:
            contador_jogador += 1
            return print(vitoria)
        if jogada_maquina == 2:
            contador_maquina += 1
            return print(derrota)

    if int_jogada == 2:
        if jogada_maquina == 0:
            contador_maquina += 1
            return print(derrota)
        if jogada_maquina == 1:
            contador_jogador += 1
            return print(vitoria)
 
while True:

    jogada = input(
            'Digite a sua jogada\n'
            '[0] Pedra, [1] Papel ou [2] Tesoura: '
               )
    
    try:    # Tratamento de erro
        int_jogada = int(jogada)
    except ValueError:
        print('Digite apenas um dos números apresentados na opções.')
        break
    if len(jogada) > 1:
        print('Digite apenas um dos números apresentados nas opções.\n')
    elif int_jogada > 2 or int_jogada < 0:
        print('Digite apenas um dos números apresentados nas opções.\n')

    try:
        confronto(int_jogada)

    except IndexError:
        continue

    print()    
    placar = print(f'Sua pontuação: {contador_jogador}\n'
                   f'Pontuação da máquina: {contador_maquina}')
    
