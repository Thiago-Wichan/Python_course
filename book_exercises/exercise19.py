# E X E R C I S E # 1 9 : P A S S W O R D G E N E R A T O R

import random
import string as s

LOWER_LETTERS = s.ascii_lowercase
UPPER_LETTERS = s.ascii_uppercase
NUMBERS = s.digits
SPECIAL = s.punctuation
TOTAL: str = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL

# password = ''.join(random.SystemRandom().choices(
#     population=(s.ascii_lowercase + s.ascii_uppercase +
#                 s.digits + s.punctuation), k=length))


def generatePassword(length: int):
    if length < 12:
        length = 12
    password = []
    password.append(LOWER_LETTERS[random.randint(0, len(LOWER_LETTERS))])
    password.append(UPPER_LETTERS[random.randint(0, len(UPPER_LETTERS))])
    password.append(NUMBERS[random.randint(0, len(NUMBERS))])
    password.append(SPECIAL[random.randint(0, len(SPECIAL))])
    while len(password) < length:
        password.append(TOTAL[random.randint(0, len(TOTAL))])
    random.shuffle(password)
    return password


assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial
print(*pw)
