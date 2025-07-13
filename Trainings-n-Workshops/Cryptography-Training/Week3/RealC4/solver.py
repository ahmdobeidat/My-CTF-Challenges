from Crypto.Util.Padding import pad
from pwn import xor
ct = bytes.fromhex("abd2d7084056965484e80d3c3609fa8fb791dd274708b870aeea01223149babd8fcc9e0a5d5fe433a6cc06071665efc395afa1773b36da0fcd9c51474b35c1ed")
pt = pad(b'}',16)
ks = xor(pt, ct[-16:])
print(xor(ks,ct))