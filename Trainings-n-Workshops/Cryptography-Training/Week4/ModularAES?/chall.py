from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, getRandomInteger
from Crypto.Util.Padding import pad, unpad

modulus = getPrime(512)
secret = getRandomInteger(12)

aes_key = pow(secret, modulus - 1, modulus)


def encrypt(data , key):
    cipher = AES.new(key.to_bytes(16, 'big'), AES.MODE_ECB)
    return cipher.encrypt(pad(data, 16))

def decrypt(data, key):
    cipher = AES.new(key.to_bytes(16, 'big'), AES.MODE_ECB)
    return unpad(cipher.decrypt(data), 16)


flag = b'CryptoCTF{REDACATED}'

ct = encrypt(flag, aes_key)

print(f'ct = {ct.hex()}')

# ct = 5cd8f92d3e0ffbb61003ae6b5898fd6c14ef9d098e23b071a80c8a49884c3225686704bb93a59ed7641b65a828d9daa3