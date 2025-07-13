from Crypto.Util.number import *
from random import randint

Primes = [getPrime(512) for _ in range(7)]
e = 65537
Ns = []

for i in range(4):
    ind1 = randint(0, 6)
    ind2 = randint(0, 6)
    Ns.append(Primes[ind1]*Primes[ind2])

flag = b'CryptoCTF{REDACTED}'

cts = []
for i in range(4):
    m = bytes_to_long(flag)
    cts.append(pow(m, e, Ns[i]))    

print(f'Ns = {Ns}')
print(f'e = {e}')
print(f'cts = {cts}')
    

