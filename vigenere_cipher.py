def vigenere_cipher(message, keyword, mode='encrypt'):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    keyword_repeated = (keyword * (len(message) // len(keyword))) + keyword[:len(message) % len(keyword)]

    for i in range(len(message)):
        if message[i].upper() in alphabet:
            msg_index = alphabet.index(message[i].upper())
            key_index = alphabet.index(keyword_repeated[i].upper())

            if mode == 'encrypt':
                new_index = (msg_index + key_index) % 26
            elif mode == 'decrypt':
                new_index = (msg_index - key_index) % 26
            else:
                raise ValueError("Invalid mode! Use 'encrypt' or 'decrypt'.")

            if message[i].isupper():
                result += alphabet[new_index]
            else:
                result += alphabet[new_index].lower()
        else:
            result += message[i]  # Keep non-alphabet characters unchanged

    return result

if __name__ == "__main__":
    mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ")
    message = input("Enter your message: ")
    keyword = input("Enter your keyword: ")

    if mode == 'encrypt':
        encrypted_message = vigenere_cipher(message, keyword, mode)
        print(f"Encrypted Message: {encrypted_message}")
    elif mode == 'decrypt':
        decrypted_message = vigenere_cipher(message, keyword, 'decrypt')
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid choice!")
