# http://en.literateprograms.org/Rot13_%28Python%29

def rot13_char(ch):
    """ Apply ROT13 to a single ASCII character. """
    if not ch.isalpha():
        return ch

    ch_low = ch.lower()
    if ch_low <= 'm':
        dist = 13
    else:
        dist = -13
    return chr(ord(ch) + dist)

def rot13(s):
    """ Apply ROT13 to a string. """
    return ''.join( rot13_char(ch) for ch in s )

