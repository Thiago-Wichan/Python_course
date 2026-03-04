
def ordinalSuffix(number):
    str_number = str(number)
    if str_number[-2:] in ('11', '12', '13'):
        return f"{str_number}th"
    elif str_number[-1:] == '1':
        return f"{str_number}st"
    elif str_number[-1:] == '2':
        return f"{str_number}nd"
    elif str_number[-1:] == '3':
        return f"{str_number}rd"
    else:
        return f"{str_number}th"


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
