# E X E R C I S E # 2 3 : 9 9 B O T T L E S O F B E E R

i = 99
# while i >= 1:
#     minus_i = i-1
#     if minus_i != 0:
#         print(f'{i} bottles of beer on the wall,\n'
#               f'{i} bottles of beer,\n'
#               'Take one down,\n'
#               'Pass it around,\n\r'
#               f'{minus_i} bottles of beer on the wall.\n'
#               )
#         i -= 1
#         continue
#     else:
#         print(f'{i} bottle of beer on the wall,\n'
#               f'{i} bottle of beer,\n'
#               'Take one down,\n'
#               'Pass it around,\n\r'
#               'No more bottles of beer on the wall!'
#               )
#         break


def bottles():
    for number_of_bottles in range(99, 1, -1):
        print(f'{number_of_bottles} bottles of beer on the wall,\n'
              f'{number_of_bottles} bottles of beer,\n'
              'Take one down,\n'
              'Pass it around,')
        if number_of_bottles - 1 == 1:
            print('1 bottle of beer on the wall,\n\r')
        else:
            print(f'{number_of_bottles-1} bottles of beer on the wall.\n\r')

    print('1 bottle of beer on the wall,\n'
          '1 bottle of beer,\n'
          'Take one down,\n'
          'Pass it around,\n\r'
          'No more bottles of beer on the wall!'
          )


bottles()
