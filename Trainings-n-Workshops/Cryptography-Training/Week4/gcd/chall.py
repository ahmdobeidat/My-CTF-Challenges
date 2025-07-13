from  Crypto.Util.number import GCD, getPrime, bytes_to_long, long_to_bytes
from random import randint

possible_keys = list(set([getPrime(15) for _ in range(256)]))
print(f'possible_keys = {possible_keys}')

keys = [possible_keys[randint(0, len(possible_keys))] for _ in range(6)]


flag = b'CryptoCTF{REDACATED}'

flag = bytes_to_long(flag)
ct = flag
for i in range(6):
    ct  *= keys[i]

print(f'ct = {ct}')