from Crypto.Cipher import AES
from Crypto.Util.number import getRandomInteger
from Crypto.Util.Padding import pad, unpad
from hashlib import sha1

key1 = getRandomInteger(24)

key2 = getRandomInteger(24)


flag = b'This is my flag CryptoCTF{REDACT}'



def encrypt(data,key):
    key = sha1(str(key).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data,16))

def decrypt(data,key):
    key = sha1(str(key).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(data),16)

ct = encrypt(encrypt(flag,key1),key2)

print(f'ct = {ct}')

# ct = b"\x07\xbcI!\x00\xc8\t\xd7.Bi35m\xbaW\xa6\x9e\xeb\x8fK\x17\x13A}\\\xa2\xf5\xe8-\xac\x1d\x7f\xb8\xa6\xa2]\x92\xf0\x02S\x1f\x1eO~\x12f\xf7Oe\x03\x95\xdc\x9b\xe4P\xa2\x08\x1e\x82\xa8\x81'\xdf\xb1\x16\xed\x07\x00U\xa5\xff\xce\xb1\x95x\xbdW\xde\xe9"