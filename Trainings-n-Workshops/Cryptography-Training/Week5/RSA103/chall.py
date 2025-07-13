from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)
n = p*p
e = 65537

flag = b'CryptoCTF{REDACTED}'


m = bytes_to_long(flag)

c = pow(m, e, n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
