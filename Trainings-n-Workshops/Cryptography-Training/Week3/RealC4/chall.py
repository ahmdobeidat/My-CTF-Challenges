from Crypto.Cipher import ARC4
from Crypto.Util.Padding import pad
import os

key = os.urandom(16)
BLOCK_SIZE = 16

flag = b'REDACTED'

padded = pad(flag,16)

blocks = [padded[i:i + BLOCK_SIZE] for i in range(0,len(padded),BLOCK_SIZE)]

ct = b''

for block in blocks:
    rc4 = ARC4.new(key)
    ct += rc4.encrypt(block)
    
print(f'ct = {ct.hex()}')

# ct = abd2d7084056965484e80d3c3609fa8fb791dd274708b870aeea01223149babd8fcc9e0a5d5fe433a6cc06071665efc395afa1773b36da0fcd9c51474b35c1ed