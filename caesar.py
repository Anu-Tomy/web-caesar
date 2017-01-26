"""

Utility methods to help in encryption.

"""

lowerLetters = 'abcdefghijklmnopqrstuvwxyz'

upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def alphabet_position(char):

    """

    Return the alphabet position.

    Returns -1 for all invalid input.

    """

    if type(char) != type(''):

        return -1

    if len(char) != 1:

        return -1

    if char.isalpha():

        return lowerLetters.find(char.lower())

    return -1



def rotate_character(char, rot):

    """

    Return the character shifted by rot amount.

    char must be a single character and rot must be a positive integer.

    char is returned AS IS if any errors, including if it is not a character

    """

    if type(char) != type(''):

        return char

    if type(rot) != type(1):

        return char



    if len(char) != 1:

        return char

    if not char.isalpha():

        return char

    letters = lowerLetters

    if char.isupper():

        letters = upperLetters



    pos = letters.find(char)

    pos += rot

    pos = pos % 26



    return letters[pos]

"""

Module for Ceaser encryption.

"""

import sys

usage = 'usage: python3 ceaser.py n'

def encrypt(text, rot):

    """

    Ceaser encryption.

    """



    if type(text) != type(''):

        raise TypeError

    if type(rot) != type(1):

        raise TypeError



    retText = ''

    for char in text:

        retText += helpers.rotate_character(char, rot)

    return retText

def user_input_is_valid(cl_args):

    if len(cl_args) !=2:

        return False

    rot = cl_args[1]

    if not rot.isdigit():

        return False

    return True

def main():

    if not user_input_is_valid(sys.argv):

        print(usage)

        sys.exit()

    text = input('Type a message:\n')

    rot = int(sys.argv[1])



    try:

        print(encrypt(text, rot))

    except:

        print(usage)

        sys.exit()
