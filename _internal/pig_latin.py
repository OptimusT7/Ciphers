import questionary
import os

vowels = 'aeiouAEIOU'

def encode(text):
  result = ""

  for word in text.split():
    if word[0] in vowels:
      result += word + "way "
    else:
      result += word[1:] + word[0] + "ay "

  return result.strip()

def decode(text):
    result = ""

    for word in text.split():
        if word.endswith("way") and word[0] in vowels:
            result += ('(' + word[:-3] + ' or ' + word[-3] + word[:-3] + ') ')
        else:
            result += word[-3] + word[:-3] + ' '

    return result.strip()


def main():
    mode = questionary.select("Select mode:", choices=["Encode", "Decipher", "Back"]).ask()

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
        print("\nEncoded Message:")
        print(encode(n_message))

    elif mode == "Decipher":
        successful = False
        while not successful:
            e_message = input("Enter the message you wish to decode:\n")
            if e_message:
                successful = True
            else:
                print("Please enter the message")
        print("\nDecoded Message:")
        print(decode(e_message))

if __name__ == "__main__":
  main()
