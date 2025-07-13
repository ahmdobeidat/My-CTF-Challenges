from pwn import xor

with open("MagicKeys/flag.jpg", "rb") as f:
    img = f.read()

key = img[:12]
flag = xor(img, key)
with open("MagicKeys/messed_up.jpg", "wb") as f:
    f.write(flag)
