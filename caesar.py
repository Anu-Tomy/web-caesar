import helpers

def encrypt(message, rot):
    """
    Ceaser encryption.
    """
    #if type(message) != type(''):
    #    raise TypeError
    #if type(rot) != type(1):
    #    raise TypeError

    retText = ''
    for char in message:
        retText += helpers.rotate_character(char, rot)
    return retText
