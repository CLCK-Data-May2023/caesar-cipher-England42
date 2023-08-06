def caesar_cipher(text, shift=5):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result

plain_text = input("Enter a sentence to encrypt: ")
encrypted_text = caesar_cipher(plain_text)
print("The encrypted text is:", encrypted_text)
