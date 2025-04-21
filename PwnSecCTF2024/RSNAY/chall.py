from Crypto.Util.number import *
from secret import flag,e,n



def encrypt(m):
    return pow(m,e,n)

assert (pow(encrypt(flag),e,n) - flag) % GCD(e,n)  == 0


menu = """Welcome to my Encryption Service! 
Choose an option:
1. Encrypt
2. Get Flag
3. Exit
"""
def main():
    encryption_counter = 0
    print(menu)
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            if encryption_counter >= 2:
                print("You have reached the maximum number of encryptions allowed!")
                break
            else:
                encryption_counter += 1
                m = int(input("Enter the message you want to encrypt: "))
                print(f"Here is your encrypted message: {encrypt(m)}")
        elif choice == '2':

            print(f"Here is your flag: {encrypt(flag)}")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
            continue


if __name__ == "__main__":
    main()
