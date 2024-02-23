import questionary
import os

mode = questionary.select("Select mode:", choices=["Encode", "Brute Decipher", "Specific Decipher"]).ask()
os.system('cls||clear')
alphabet = 'abcdefghijklmnopqrstuvwxyz'*3
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# natural message
n_message = ''

# encoded message
e_message = ''

# encode factor
factor = 0

if mode == "Encode":
    successful = False
    while not successful:
        n_message = input("Enter the message you wish to encode:\n")
        if n_message:
            successful = True
        else:
            print("Please enter the message")
    successful = False
    while not successful:
        factor = input("\nEnter encode factor (e.g. 3, -2): ").strip()
        try:
            factor = int(factor)
        except:
            print("Please enter an integer")
        else:
            if factor % 26 != 0:
                successful = True
                factor = int(factor) % 26
            else:
                print("The encode factor you entered is just 0")
    e_alphabet = alphabet[26+factor:52+factor]
    print("Encoded Message:")
    for char in n_message:
        if char in alphabet:
            print(e_alphabet[alphabet.index(char)], end="")
        elif char in caps:
            print(e_alphabet[alphabet.index(char.lower())].upper(), end="")
        else:
            print(char, end="")

elif mode == "Brute Decipher":
    # encoded message
    successful = False
    while not successful:
        e_message = input("Enter the message you wish to decode:\n")
        if e_message:
            successful = True
        else:
            print("Please enter the message")
    print()
    for factor in range(26):
        factor -= 12
        if factor != 0:
            s_factor = str(factor)
            if s_factor[0] != '-':
                s_factor = '+' + s_factor
            print(f"Factor: {s_factor}")
            for char in e_message:
                if char in alphabet:
                    print(alphabet[alphabet.index(char)-factor], end="")
                elif char in caps:
                    print(alphabet[alphabet.index(char.lower())-factor].upper(), end="")
                else:
                    print(char, end="")
            print()
        print()

elif mode == "Specific Decipher":
    successful = False
    while not successful:
        e_message = input("Enter the message you wish to decode:\n")
        if e_message:
            successful = True
        else:
            print("Please enter the message")
    successful = False
    while not successful:
        factor = input("\nEnter encode factor of original message (e.g. 3, -2): ").strip()
        try:
            factor = int(factor)
        except:
            print("Please enter an integer")
        else:
            if factor % 26 != 0:
                successful = True
                factor = int(factor) % 26
            else:
                print("The encode factor you entered is just 0")
    e_alphabet = alphabet[26 + factor:52 + factor]
    print("Decoded Message:")
    for char in e_message:
        if char in alphabet:
            print(alphabet[e_alphabet.index(char)], end="")
        elif char in caps:
            print(alphabet[e_alphabet.index(char.lower())].upper(), end="")
        else:
            print(char, end="")
