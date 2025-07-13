from Crypto.Util.number import *
from matplotlib.artist import getp

p = getPrime(512)
q = getPrime(512)
r = getPrime(512)
k = getPrime(512)

n = p*q*r*k
e = 65537
    
flag = b'CryptoCTF{REDACTED}'

m = bytes_to_long(flag)

c = pow(m, e, n)

print(f'e = {e}')
print(f'c = {c}')
print(f'r = {r}')
print(f'p = {p}')
print(f'q = {q}')
print(f'k = {k}')


