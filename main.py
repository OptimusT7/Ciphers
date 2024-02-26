import questionary
import os

while True:
    cipher = questionary.select("Select Cipher:", choices=["Caesar", "Atbash", "Rail-Fence", "Columnar", "Playfair", "Letter-Number", "Morse Code"]).ask()
    if cipher == "Caesar":
        os.system('cls||clear')
        import _internal.caesar

    elif cipher == "Atbash":
        os.system('cls||clear')
        import _internal.atbash

    elif cipher == "Rail-Fence":
        os.system('cls||clear')
        import _internal.rail_fence

    elif cipher == "Columnar":
        os.system('cls||clear')
        import _internal.columnar

    elif cipher == "Playfair":
        os.system('cls||clear')
        import _internal.playfair

    elif cipher == "Letter-Number":
        os.system('cls||clear')
        import _internal.letter_number

    elif cipher == "Morse Code":
        os.system('cls||clear')
        import _internal.morse

    print('\n\n')
