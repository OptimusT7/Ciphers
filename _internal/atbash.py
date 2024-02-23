import questionary
import os

mode = questionary.select("Select mode:", choices=["Encode", "Decipher"]).ask()
os.system('cls||clear')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# natural message
n_message = ''

# encoded message
e_message = ''

if mode == "Encode":
    successful = False
    while not successful:
        n_message = input("Enter the message you wish to encode:\n")
        if n_message:
            successful = True
        else:
            print("Please enter the message")
    successful = False

    print("\nEncoded Message:")
    for char in n_message:
        if char in alphabet:
            print(alphabet[-(alphabet.index(char)) - 1], end="")
        elif char in caps:
            print(alphabet[-(alphabet.index(char.lower())) - 1].upper(), end="")
        else:
            print(char, end="")

elif mode == "Decipher":
    successful = False
    while not successful:
        e_message = input("Enter the message you wish to decode:\n")
        if e_message:
            successful = True
        else:
            print("Please enter the message")
    print("\nDecoded Message:")
    for char in e_message:
        if char in alphabet:
            print(alphabet[-(alphabet.index(char)) - 1], end="")
        elif char in caps:
            print(alphabet[-(alphabet.index(char.lower())) - 1].upper(), end="")
        else:
            print(char, end="")
