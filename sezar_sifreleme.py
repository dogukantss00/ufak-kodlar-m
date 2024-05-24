def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            result += char

    return result

plain_text = "Hello, CTF!"
shift_value = 3
cipher_text = caesar_cipher(plain_text, shift_value)

print(f"Plain Text: {plain_text}")
print(f"Cipher Text: {cipher_text}")