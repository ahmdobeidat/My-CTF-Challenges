from secret import flag,f, integrate
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256

key = f'{integrate(f, 2.420, 1.77415).evalf():.2f}'
print(key)

def encrypt(key, data):
    key = sha256(str(key).encode('utf-8')).digest()[16:]
    iv =  sha256(str(key).encode('utf-8')).digest()[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv = iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return ct_bytes

ct = encrypt(key, flag)

def get_hint(x):
    return f(x)
def get_flag():
    return ct.hex()

def main():
    print("Welcome to my secure encryption service!")
    print("")
    hint_ctr = 0
    while True:
        try:
            option = int(input("1. Get hint\n2. Get flag\n3. Exit\n"))
            if option == 1:
                if hint_ctr > 2:
                    print("You have exceeded the maximum number of hints.")
                    continue
                hint_ctr += 1
                x = float(input("Enter a number: "))
                print(get_hint(x))
            elif option == 2:
                print(f"Here is the flag: {get_flag()}")
            elif option == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except:
            print("An error occurred. Please try again.")
            continue
if __name__ == '__main__':
    main()
