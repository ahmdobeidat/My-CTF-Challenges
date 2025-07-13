from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime


p = getPrime(434)

flag = b'CryptoCTF{REDACATED}'

flag = bytes_to_long(flag)

ct = flag % p
print(f'bit length of flag: {flag.bit_length()}')
print(f'p = {p}')
print(f'ct = {ct}')
