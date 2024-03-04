import questionary
import os

def encode(text, rails):
    # Create a matrix to store the zig-zag pattern
    matrix = [['' for _ in range(len(text))] for _ in range(rails)]

    # Variables to mark the direction of movement
    down = False
    row, col = 0, 0

    # Fill the zigzag pattern in the matrix
    for char in text:
        if (row == 0) or (row == rails - 1):
            down = not down
        matrix[row][col] = char
        col += 1
        row += 1 if down else -1

    # Extract the encoded text from the matrix
    result = []
    for i in range(rails):
        for j in range(len(text)):
            if matrix[i][j] != '':
                result.append(matrix[i][j])
    return ''.join(result)

def decode(e_text, rails):
    # Calculate the length of the original message
    length = len(e_text)

    # Create a matrix with the same dimensions as the one used for encoding
    matrix = [['' for _ in range(length)] for _ in range(rails)]

    # Mark the positions in the matrix where the characters of the original message would have been placed during the encoding process
    down = False
    row, col = 0, 0
    for _ in range(length):
        if (row == 0) or (row == rails - 1):
            down = not down
        matrix[row][col] = '*'
        col += 1
        row += 1 if down else -1

    # Fill these marked positions with the characters from the encoded message in the order they appear
    index = 0
    for i in range(rails):
        for j in range(length):
            if matrix[i][j] == '*':
                matrix[i][j] = e_text[index]
                index += 1

    result = []
    down = False
    row, col = 0, 0
    for _ in range(length):
        if (row == 0) or (row == rails - 1):
            down = not down
        result.append(matrix[row][col])
        col += 1
        row += 1 if down else -1

    return ''.join(result)

def main():
    mode = questionary.select("Select mode:", choices=["Encode", "Brute Decipher", "Specific Decipher", "Back"]).ask()

    # natural message
    n_message = ''

    # encoded message
    e_message = ''

    # encode rails
    rails = 0

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
            rails = input("\nEnter the number of rails: ").strip()
            try:
                rails = int(rails)
            except:
                print("Please enter an integer")
            else:
                if rails != 0:
                    successful = True
                else:
                    print("The number of rails you entered is just 0")

        print(encode(n_message, rails))

    elif mode == "Brute Decipher":
        successful = False
        while not successful:
            e_message = input("Enter the message you wish to decode:\n")
            if e_message:
                successful = True
            else:
                print("Please enter the message")
        print()
        for rails in range(2, len(e_message)):
            print(f"Rails: {rails}")
            print(decode(e_message, rails))
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
            rails = input("\nEnter the number of rails: ").strip()
            try:
                rails = int(rails)
            except:
                print("Please enter an integer")
            else:
                if rails != 0:
                    successful = True
                else:
                    print("The number of rails you entered is just 0")

        print(decode(e_message, rails))

if __name__ == "__main__":
  main()
