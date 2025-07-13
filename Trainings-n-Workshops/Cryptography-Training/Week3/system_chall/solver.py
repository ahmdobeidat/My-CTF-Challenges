from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha1
import sympy as sp


ct = b'#K\xb0\x8c\xd6\xa7\x8e"\xd1\xdc\xb1s\x83\xd3\x07A\xa5\xd0\xdc;\xe9"\x1e\x93\x9a\xb3\xd0`@{\r\x80\xe1\x8c%iG\xc6S0}V3\xf57\x07\xf2\x9e'

def decrypt(data,key):
    key = sha1(str(key).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(data),16)

x = sp.symbols('x')
y = sp.symbols('y')

eq1 = sp.Eq(4*x + 7*y, 2065)
eq2 = sp.Eq(77*x + 5*y, 32615)

sol = sp.solve((eq1, eq2), (x, y))

private_key1 = sol[x]

private_key2 = sol[y]

key = private_key1 * private_key2
print(private_key1, private_key2)

print(decrypt(ct,key))