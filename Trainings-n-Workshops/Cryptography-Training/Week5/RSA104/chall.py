from calendar import c
from Crypto.Util.number import *

p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537
phi = (p+1)*(q+1)

flag = b'CryptoCTF{REDACTED}'

m = bytes_to_long(flag)

c = pow(m, e, n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
print(f'phi = {phi}')