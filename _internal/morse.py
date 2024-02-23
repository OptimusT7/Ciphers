import questionary
import os

mode = questionary.select("Select mode:", choices=["Encode", "Decipher"]).ask()
os.system('cls||clear')
alphabet = [
    (' ', '/ '),
    ('1', '.----  '),
    ('2', '..---  '),
    ('3', '...--  '),
    ('4', '....-  '),
    ('5', '.....  '),
    ('6', '-....  '),
    ('7', '--...  '),
    ('8', '---..  '),
    ('9', '----.  '),
    ('0', '-----  '),
    ('b', '-...  '),
    ('c', '-.-.  '),
    ('f', '..-.  '),
    ('h', '....  '),
    ('j', '.---  '),
    ('l', '.-..  '),
    ('p', '.--.  '),
    ('q', '--.-  '),
    ('v', '...-  '),
    ('x', '-..-  '),
    ('y', '-.--  '),
    ('z', '--..  '),
    ('d', '-..  '),
    ('g', '--.  '),
    ('k', '-.-  '),
    ('o', '---  '),
    ('r', '.-.  '),
    ('s', '...  '),
    ('u', '..-  '),
    ('w', '.--  '),
    ('a', '.-  '),
    ('i', '..  '),
    ('m', '--  '),
    ('n', '-.  '),
    ('e', '.  '),
    ('t', '-  ')
]

# natural message
n_message = ''

# encoded message
e_message = ''

if mode == "Encode":
    successful = False
    while not successful:
        n_message = input("Enter the message you wish to encode:\n").lower()
        if n_message:
            successful = True
        else:
            print("Please enter the message")
    successful = False
    e_message = n_message
    print("\nEncoded Message:")
    for (x, y) in alphabet:
        e_message = e_message.replace(x, y)
    print(e_message[:-2])


elif mode == "Decipher":
    successful = False
    while not successful:
        e_message = input("Enter the message you wish to decode:\n")
        if e_message:
            successful = True
        else:
            print("Please enter the message")
    successful = False
    if e_message[-1] != '  ':
        e_message += '  '
    n_message = e_message
    print("\nDecoded Message:")
    for (x, y) in alphabet:
        n_message = n_message.replace(y, x)
    print(n_message)
