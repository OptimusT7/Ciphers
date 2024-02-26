import questionary
import os

mode = questionary.select("Select mode:", choices=["Encode", "Decipher\n", "Back"]).ask()
os.system('cls||clear')
alphabet = [
    (' ', '0;'),
    ('j', '10;'),
    ('k', '11;'),
    ('l', '12;'),
    ('m', '13;'),
    ('n', '14;'),
    ('o', '15;'),
    ('p', '16;'),
    ('q', '17;'),
    ('r', '18;'),
    ('s', '19;'),
    ('t', '20;'),
    ('u', '21;'),
    ('v', '22;'),
    ('w', '23;'),
    ('x', '24;'),
    ('y', '25;'),
    ('z', '26;'),
    ('a', '1;'),
    ('b', '2;'),
    ('c', '3;'),
    ('d', '4;'),
    ('e', '5;'),
    ('f', '6;'),
    ('g', '7;'),
    ('h', '8;'),
    ('i', '9;')
]

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
    e_message = n_message
    print("\nEncoded Message:")
    for (x, y) in alphabet:
        e_message = e_message.replace(x, y)
    print(e_message[:-1])


elif mode == "Decipher":
    successful = False
    while not successful:
        e_message = input("Enter the message you wish to decode:\n")
        if e_message:
            successful = True
        else:
            print("Please enter the message")
    successful = False
    if e_message[-1] != ';':
        e_message += ';'
    n_message = e_message
    print("\nDecoded Message:")
    for (x, y) in alphabet:
        n_message = n_message.replace(y, x)
    print(n_message)
