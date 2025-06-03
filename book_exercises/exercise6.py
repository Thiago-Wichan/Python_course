# E X E R C I S E # 6 : O R D I N A L S U F F I X

def ordinalSuffix(number: int):
    number_str = str(number)
    if number < 10:
        if number_str[-1] == '1':
            return f'{number_str}st'
        elif number_str[-1] == '2':
            return f'{number_str}nd'
        elif number_str[-1] == '3':
            return f'{number_str}rd'
        else:
            return f'{number_str}th'
    else:
        if number_str[-2] == '1':
            return f'{number_str}th'
        elif number_str[-1] == '1':
            return f'{number_str}st'
        elif number_str[-1] == '2':
            return f'{number_str}nd'
        elif number_str[-1] == '3':
            return f'{number_str}rd'
        else:
            return f'{number_str}th'


assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
