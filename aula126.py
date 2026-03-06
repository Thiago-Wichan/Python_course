questions = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def questionary():
    i = 0
    hits = 0
    errors = 0
    while i < len(questions):

        useQuestion = questions[i]
        print(f'{useQuestion['Pergunta']}\n')

        for n in range(len(useQuestion['Opções'])):
            print(useQuestion['Opções'][n])

        print('')
        answer = input('Qual a resposta correta? ')
        print('')

        if answer == useQuestion['Resposta']:
            print('Você acertou \U0001F929 \n')
            i += 1
            hits += 1

        else:
            print('Você errou \U0001FAE0 \n')
            i += 1
            errors += 1

    if errors == 0:
        return f'Parabéns! Você acertou todas as {len(questions)} questões.'

    if hits == 0:
        return f'Você errou todas as {len(questions)} questões.'

    return f'Você acertou {hits} e errou {errors} de {len(questions)} questões'


print(questionary())
