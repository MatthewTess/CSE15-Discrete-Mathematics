def encode(t, k):
    result = ""
    for char in t:
        if char == ' ':
            result += char
        elif char.isupper():
            result += chr((ord(char) + k - 65) % 26 + 65)
        else:
            result += chr((ord(char) + k - 97) % 26 + 97)
    return result

def decode():
    ciphertext = input("Enter the encrypted message: ")
    shift = int(input("Enter the shift value: "))
    space = []
    ciphertext = ciphertext.split()
    message = []
    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        message.append(plaintext)
    message = ' '.join(message)
    print("Decrypted message: ", message)

t = input("Enter your message: ")
k = int(input("Enter the shift amount: "))

print("Original Message:", t)
print("Shift Amount:", str(k))
print("Cipher: " + encode(t, k))
decode()
