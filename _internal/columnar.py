import questionary
import os

def encode(text, columns):
    # Calculate the number of rows
    rows = len(text) // columns
    if len(text) % columns != 0:
        rows += 1

    # Create a matrix to store the columnar pattern
    matrix = [['' for _ in range(columns)] for _ in range(rows)]

    # Fill the columnar pattern in the matrix
    index = 0
    for row in range(rows):
        for col in range(columns):
            if index < len(text):
                matrix[row][col] = text[index]
                index += 1

    # Extract the encoded text from the matrix
    result = []
    for col in range(columns):
        for row in range(rows):
            if matrix[row][col] != '':
                result.append(matrix[row][col])
    return ''.join(result)

def decode(e_text, columns):
    # Calculate the number of rows
    rows = len(e_text) // columns
    if len(e_text) % columns != 0:
        rows += 1

    # Create a matrix with the same dimensions as the one used for encoding
    matrix = [['' for _ in range(columns)] for _ in range(rows)]

    # Fill the matrix with the characters from the encoded text
    index = 0
    for col in range(columns):
        for row in range(rows):
            if index < len(e_text):
                matrix[row][col] = e_text[index]
                index += 1

    # Extract the decoded text from the matrix
    result = []
    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] != '':
                result.append(matrix[row][col])
    return ''.join(result)

def main():
    mode = questionary.select("Select mode:", choices=["Encode", "Brute Decipher", "Specific Decipher", "Back"]).ask()

    # natural message
    n_message = ''

    # encoded message
    e_message = ''

    # encode columns
    columns = 0


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
            columns = input("\nEnter the number of columns: ").strip()
            try:
                columns = int(columns)
            except:
                print("Please enter an integer")
            else:
                if columns != 0:
                    successful = True
                else:
                    print("The number of columns you entered is just 0")

        print(encode(n_message, columns))

    elif mode == "Brute Decipher":
        successful = False
        while not successful:
            e_message = input("Enter the message you wish to decode:\n")
            if e_message:
                successful = True
            else:
                print("Please enter the message")
        print()
        for columns in range(2, len(e_message)):
            print(f"Columns: {columns}")
            print(decode(e_message, columns))
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
            columns = input("\nEnter the number of columns: ").strip()
            try:
                columns = int(columns)
            except:
                print("Please enter an integer")
            else:
                if columns != 0:
                    successful = True
                else:
                    print("The number of columns you entered is just 0")

        print(decode(e_message, columns))

if __name__ == "__main__":
  main()
