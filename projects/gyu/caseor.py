def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Choose:\n1. Encrypt\n2. Decrypt\n> ")

    text = input("Enter text: ")
    shift = int(input("Enter shift (key): "))

    if choice == '1':
        print("Encrypted Text:", encrypt(text, shift))
    elif choice == '2':
        print("Decrypted Text:", decrypt(text, shift))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
