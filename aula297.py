# Secrets gera números aleatórios e seguros.

# import secrets
import string as s
from secrets import SystemRandom as Sr

password_generator = (
    ''.join((Sr().choices(s.ascii_letters + s.digits +
            s.punctuation, k=100)))
)
password_generator_2 = ''.join(Sr().choices(
    ('a', 'b', 'c', 'd'), weights=[2, 3, 4, 1], k=2))
print(password_generator)
