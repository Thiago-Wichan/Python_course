# Sistema de perguntas e respostas

perguntas =[ 
    {
        'Pergunta': 'Quanto é 2x2?',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5?',
        'Opções': ['25', '55', '60', '100'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '10', '20'],
        'Resposta': '5',
    }
]

p1 = perguntas[0]
p2 = perguntas[1]
p3 = perguntas[2]
global os
contador = 0

def question(x):
    global contador
    
    print('Pergunta:', x['Pergunta'])
    print()

    for opcoes in x['Opções']:
        print(opcoes) 
    print()

    resposta = input('Qual a resposta correta? ')
    if resposta == x['Resposta']:
        acerto = print(f'Você acertou!')
        contador += 1
        return acerto
    else:
        erro = print(f'Você errou!')
        return erro
    


question(p1)
print()
question(p2)
print()
question(p3)
print()
print(f'Parabéns! Você acertou {contador} questões de', len(perguntas))


