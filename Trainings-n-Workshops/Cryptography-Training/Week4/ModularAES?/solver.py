from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad



def encrypt(data , key):
    cipher = AES.new(key.to_bytes(16, 'big'), AES.MODE_ECB)
    return cipher.encrypt(pad(data, 16))

def decrypt(data, key):
    cipher = AES.new(key.to_bytes(16, 'big'), AES.MODE_ECB)
    return unpad(cipher.decrypt(data), 16)



ct = bytes.fromhex("5cd8f92d3e0ffbb61003ae6b5898fd6c14ef9d098e23b071a80c8a49884c3225686704bb93a59ed7641b65a828d9daa3")

pt = decrypt(ct, 1)
print(pt)