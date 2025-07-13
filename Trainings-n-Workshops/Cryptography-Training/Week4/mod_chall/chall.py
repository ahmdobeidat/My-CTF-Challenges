from Crypto.Util.number import getPrime,getRandomInteger,bytes_to_long
from sympy import factorint
from secret import flag

num = bytes_to_long(flag)
f = factorint(num)
factors = list(f.keys())
n = getPrime(1024)

print(f"n = {n}")
for factor in factors :
    factor = getRandomInteger(512) * n + factor
    print(f"factor = {factor}")