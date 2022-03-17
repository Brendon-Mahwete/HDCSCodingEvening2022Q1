# A program to encode words in morse code
MORSE_CODE_DICTIONARY = {'A': '.-', 'B': '-...',
                         'C': '-.-.', 'D': '-..', 'E': '.',
                         'F': '..-.', 'G': '--.', 'H': '....',
                         'I': '..', 'J': '.---', 'K': '-.-',
                         'L': '.-..', 'M': '--', 'N': '-.',
                         'O': '---', 'P': '.--.', 'Q': '--.-',
                         'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--',
                         'X': '-..-', 'Y': '-.--', 'Z': '--..',
                         '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....',
                         '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ',': '--..--', '.': '.-.-.-',
                         '?': '..--..', "'": '.----.', '!': "-.-.--",
                         '/': '-..-.', '(': '-.--.', ')': '-.--.-',
                         '&': '.-...', ':': '---...', ';': '-.-.-.',
                         '=': '-...-', '+': '.-.-.', '-': '-....-',
                         '_': '..--.-', '"': '.-..-.', '$': '...-..-',
                         '@': '.--.-.', '¿': '..-.-', '¡': '--...-',
                         ' ': '/'}


# A function to encode words to morse code
def encode(word):
    word = word.upper()
    morse_code = ""

    """Runs each letter in the word to find it corresponding morse code in the dict and the code to 
    the variable morse_code"""
    for letter in word:
        morse_code += f"{MORSE_CODE_DICTIONARY[letter]} "

    return morse_code


# A function to decode morse code to words
def decode(coded_word):
    list = []
    new_word = ""
    # Takes the morse code that is separated by space int a list or morse code
    for symbol in coded_word:
        if symbol == " ":
            list.append(new_word)
            new_word = ""
        else:
            new_word += symbol
    # The loop doesn't append the last part of the morse code so this line of code appends it
    list.append(new_word)

    # Takes each value(morse code) in the list and finds it corresponding key
    decoded_word = ""
    for content in list:
        for key, value in MORSE_CODE_DICTIONARY.items():
            if content == value:
                decoded_word += key

    return decoded_word


while True:
    print("Please select an option by entering the menu number:")
    user_selection = int(input("1. Encrypt to Morse Code \n2. Decrypt from Morse Code \n0. Exit : "))
    if user_selection == 0:
        break
    elif user_selection == 1:
        the_word = input("Enter the message that you want to encode: ")
        print(encode(the_word))
    else:
        the_code = input("Enter the code that you want to decode: ")
        print(decode(the_code))
