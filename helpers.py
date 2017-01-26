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
