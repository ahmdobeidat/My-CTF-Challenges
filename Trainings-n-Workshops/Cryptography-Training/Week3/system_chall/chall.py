from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha1

private_key1 = ??
private_key2 = ??

assert private_key1 * 4 + private_key2 * 7 == 2065

assert private_key1 * 77 + private_key2 * 5 == 32615


key = private_key1 * private_key2



flag = b'CryptoCTF{REDACTED}'

def encrypt(data,key):
    key = sha1(str(key).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data,16))

def decrypt(data,key):
    key = sha1(str(key).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(data),16)


ct = encrypt(flag,key)

print(ct)

# ct = b'#K\xb0\x8c\xd6\xa7\x8e"\xd1\xdc\xb1s\x83\xd3\x07A\xa5\xd0\xdc;\xe9"\x1e\x93\x9a\xb3\xd0`@{\r\x80\xe1\x8c%iG\xc6S0}V3\xf57\x07\xf2\x9e'