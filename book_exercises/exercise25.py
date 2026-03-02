# E X E R C I S E # 2 5 : M U L T I P L I C A T I O N T A B L E

# n = 10
# m = list(list(range(1*i, (n+1)*i, i)) for i in range(1, n+1))
# max_width = len(str(m[-1][-1])) + 1
# for i in m:
#     i = [str(j).rjust(max_width) for j in i]
#     print(''.join(i))

print('  |  1   2   3   4   5   6   7   8   9  10')
print('--+---------------------------------------')

for column in range(1, 11):
    print(str(column).rjust(2) + '|', end='')
    for row in range(1, 11):
        print(str(column * row).rjust(3) + ' ', end='')
    print()
