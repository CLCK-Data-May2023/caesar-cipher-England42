def caesar_cipher(text, shift=5):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            # Determine whether the character is lowercase or uppercase and set the base ASCII value
            base = ord('a') if char.islower() else ord('A')
            # Encrypt the character and add to the result
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            # If not alphabetic, just add the original character to the result
            encrypted_text += char

    return encrypted_text

# Ask user for input
plain_text = input("Please enter a sentence:")
encrypted_text = caesar_cipher(plain_text)
print("The encrypted sentence is:", encrypted_text)
