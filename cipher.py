import string

def encrypt_with_shift_5(text):
    """
    Encrypt the text with a Caesar cipher using a shift of 5.
    """
    encrypted_text = []
    
    for char in text:
        # If the character is an uppercase letter
        if char in string.ascii_uppercase:
            encrypted_text.append(string.ascii_uppercase[(string.ascii_uppercase.index(char) + 5) % 26])
        # If the character is a lowercase letter
        elif char in string.ascii_lowercase:
            encrypted_text.append(string.ascii_lowercase[(string.ascii_lowercase.index(char) + 5) % 26])
        # If the character is not a letter (e.g. punctuation, spaces)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)

# Now, let's create a pytest test function to test our encryption function
import pytest

@pytest.mark.parametrize("original_sentence,encrypted_sentence",
                              [['python is fun!', 'udymts nx kzs!'],
                              ['aaa', 'fff'],
                              ['xyz', 'cde'],
                              ['A sentence with Capital letters.', 'f xjsyjshj bnym hfunyfq qjyyjwx.'],
                              ['#$%^&*()', '#$%^&*()']
                              ])
def test_encrypt_with_shift_5(original_sentence, encrypted_sentence):
    assert encrypt_with_shift_5(original_sentence) == encrypted_sentence
