from Crypto.Cipher import AES
from Crypto.Util.number import getRandomInteger
from Crypto.Util.Padding import pad, unpad
from hashlib import sha1

public_key = getRandomInteger(12)

private_key = getRandomInteger(12)


flag = b'ptoCTF{REDACTED}'
padded = b'ptoCTF{REDACTED}\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'
def encrypt(data,key):
    key = sha1(str(key).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data,16))
print(unpad(padded,16))

def decrypt(data,key):
    key = sha1(str(key).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(data),16)


ct = encrypt(flag,private_key * public_key)

print(f'ct = {ct}')
print(f'public_key = {public_key}')