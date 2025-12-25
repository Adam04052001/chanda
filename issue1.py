#import doctest
"""Morse Code Translator"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе
    
    #>>> encode('SOS')
    '... --- ...'
    
    #>>> encode('CHANDA')
    '-.-. .... .- -. -.. .-'
    
    #>>> encode('O' * 30) #doctest: +ELLIPSIS
    ('--- ... ---')
    #>>> encode('ф')
    KeyError                                
    Traceback (most recent call last)
    KeyError 'ф' 
    
    #>>> encode(%)
    SyntaxError: invalid syntax
    
    #>>> encode(True)
    Traceback (most recent call last)
    TypeError: 'bool' object is not iterable
    """
    
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)

def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """
    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


# if __name__ == '__main__':
#    doctest.testmod()

if __name__ == '__main__':
    morse_motto = '... .... .. -. .   -... ..- -   -. --- -   -... ..- .-. -.   --- ..- -'
    decoded_motto = decode(morse_motto)
    print(decoded_motto)
    err_msg = f'{morse_motto} != {encode(decoded_motto)}'
    assert morse_motto == encode(decoded_motto), err_msg

#print('Hello, Islam')