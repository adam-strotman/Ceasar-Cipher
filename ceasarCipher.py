import random

alphabet_lower = "abcdefghijklmnopqrstuvwxyz "
alphabet_upper = alphabet_lower.upper()
letter_to_index = dict(zip(alphabet_lower, range(len(alphabet_lower))))
index_to_letter = dict(zip(range(len(alphabet_lower)), alphabet_lower))


def encrypt(message, key):
    cipher = ''

    for letter in message:
        number = (letter_to_index[letter] + key) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher


def decrypt(cipher, key):
    decrypted = ''

    for letter in cipher:
        number = (letter_to_index[letter] - key) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted


def main():
    message = input('Enter Message: ')
    key = random.randint(1, 100)  # int(input('Enter key: '))
    cipher = encrypt(message, key)
    decrypted = decrypt(cipher, key)

    print('Original message: ' + message)
    print('Encrypted message: ' + cipher)
    print('Decrypted message: ' + decrypted)


main()
