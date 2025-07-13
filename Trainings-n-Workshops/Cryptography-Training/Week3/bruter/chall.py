from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha1

key = 'REDACTED'.lower().encode()

flag = b'CryptoCTF{REDACTED}'

def encrypt(data,key):
    key = sha1(key).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data,16))

def decrypt(data,key):
    key = sha1(key).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(data),16)




#ct = b"\xf2:\xa9\x88\\\x8f.\x94\xbc\xcf\x13\xfdL8<\\\x81\xbe\x0f\t\x82\x88K\xd4,o\x8eGEn\x037\x03\xabb\x91\x13\xb0'\xe4\xb1\xf5\xdf\x1b\xe7Q\x1e\xac"

ct = encrypt(flag,key)

print(ct)