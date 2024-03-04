import questionary
import os

import _internal.caesar
import _internal.atbash
import _internal.rail_fence
import _internal.columnar
import _internal.playfair
import _internal.letter_number
import _internal.morse
import _internal.pig_latin

history = 'Show'
show_history = False
skip = False

while True:
    if not show_history:
        os.system('cls||clear')
    cipher = questionary.select("Select Cipher:", choices=["Atbash", "Caesar", "Columnar", "Letter-Number", "Morse Code", "Pig Latin", "Playfair", "Rail-Fence\n", f"{history} History"]).ask()
    if cipher == "Caesar":
        if not show_history:
            os.system('cls||clear')
        _internal.caesar.main()

    elif cipher == "Atbash":
        if not show_history:
            os.system('cls||clear')
        _internal.atbash.main()

    elif cipher == "Rail-Fence\n":
        if not show_history:
            os.system('cls||clear')
        _internal.rail_fence.main()

    elif cipher == "Columnar":
        if not show_history:
            os.system('cls||clear')
        _internal.columnar.main()

    elif cipher == "Playfair":
        if not show_history:
            os.system('cls||clear')
        _internal.playfair.main()

    elif cipher == "Letter-Number":
        if not show_history:
            os.system('cls||clear')
        _internal.letter_number.main()

    elif cipher == "Morse Code":
        if not show_history:
            os.system('cls||clear')
        _internal.morse.main()

    elif cipher == "Pig Latin":
        if not show_history:
            os.system('cls||clear')
        _internal.pig_latin.main()
        
    elif cipher == f"{history} History":
        if show_history:
            show_history = False
            history = 'Show'
        else:
            show_history = True
            history = 'Hide'
            os.system('cls||clear')
        skip = True

    if not skip:
        print('\n')
        choice = questionary.select("Continue?", choices=["Yes", "No"]).ask()
        if choice == "No":
            break
    skip = False
