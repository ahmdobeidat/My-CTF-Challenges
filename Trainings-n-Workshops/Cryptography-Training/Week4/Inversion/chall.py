from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime



p = getPrime(512)
coeffs = [getPrime(15) for _ in range(2)]
flag = b'CryptoCTF{REDACTED}'
flag = bytes_to_long(flag)
ct = pow(flag , -1, p)

print(f'p = {p * coeffs[0] * coeffs[1]}')
print(f'ct = {ct * coeffs[0] * coeffs[1]}')