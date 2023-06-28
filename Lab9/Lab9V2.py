def encode(t, k):
    result = ""
    for char in t:
        encoded_char = chr((ord(char) + k - 32) % 94 + 32)
        result += encoded_char
    return result

def decode(t, k):
    result = ""
    for char in t:
        decoded_char = chr((ord(char) - k - 32) % 94 + 32)
        result += decoded_char
    return result

t = input("Input the message you want encoded: ")
k = int(input("Enter your shift amount: "))
print("Encrypted Message: " + encode(t, k))

t = input("Input the message you want decoded: ")
k = int(input("Enter your shift amount: "))
print("Decrypted Message: " + decode(t, k))
