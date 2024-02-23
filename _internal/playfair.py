import questionary
import os
import math

mode = questionary.select("Select mode:", choices=["Encode", "Decipher"]).ask()
os.system('cls||clear')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# natural message
n_message = ''

# encoded message
e_message = ''

# keyword used to decipher the message
keyword = ''


def generate_matrix(keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    matrix = [[None] * 5 for _ in range(5)]
    keyword = keyword.replace('j', 'i')
    keyword += ''.join(sorted(set(alphabet) - set(keyword)))
    keyword = keyword[:25]
    for i, char in enumerate(keyword):
        matrix[i // 5][i % 5] = char
    return matrix

def prepare_text(text):
    text = text.replace('j', 'i')
    text = ''.join(c for c in text if c.isalpha())  # remove non-alphabetic characters
    pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            pairs.append(text[i] + 'x')
        elif text[i] == text[i + 1]:
            pairs.append(text[i] + 'x')
            i -= 1
        else:
            pairs.append(text[i:i + 2])
        i += 2
    return pairs


def encode_pair(pair, matrix):
    row1, col1, row2, col2 = None, None, None, None
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == pair[0]:
                row1, col1 = i, j
            if matrix[i][j] == pair[1]:
                row2, col2 = i, j
    if row1 is None or col1 is None or row2 is None or col2 is None:
        return 'xx'  # Return a placeholder value
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encode(text, keyword):
    text = text.lower()  # Convert to lowercase
    keyword = keyword.lower()  # Convert to lowercase
    matrix = generate_matrix(keyword)
    text_pairs = prepare_text(text)
    encoded_text = ''
    for pair in text_pairs:
        encoded_text += encode_pair(pair, matrix)
    return encoded_text

def decode_pair(pair, matrix):
    row1, col1, row2, col2 = None, None, None, None
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == pair[0]:
                row1, col1 = i, j
            if matrix[i][j] == pair[1]:
                row2, col2 = i, j
    if row1 is None or col1 is None or row2 is None or col2 is None:
        return 'xx'  # Return a placeholder value
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decode(text, keyword):
    text = text.lower()  # Convert to lowercase
    keyword = keyword.lower()  # Convert to lowercase
    matrix = generate_matrix(keyword)
    text_pairs = prepare_text(text)
    decoded_text = ''
    for pair in text_pairs:
        decoded_text += decode_pair(pair, matrix)
    return decoded_text


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
        keyword = input("\nEnter the keyword: ")
        if keyword:
            successful = True
        else:
            print("Please enter the keyword")
    print(encode(n_message, keyword))


elif mode == "Decipher":
    # encoded message
    successful = False
    while not successful:
        e_message = input("Enter the message you wish to decode:\n")
        if e_message:
            successful = True
        else:
            print("Please enter the message")
    successful = False
    while not successful:
        keyword = input("\nEnter the keyword: ")
        if keyword:
            successful = True
        else:
            print("Please enter the keyword")
    print(decode(e_message, keyword))
