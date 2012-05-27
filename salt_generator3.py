#1/usr/bin/env python3.2
from random import SystemRandom
from sys import argv, stderr, exit

__desc__ = 'This program prints a Python 3 bytes object of random bytes useful for static cryptographic hash salts.'

commonerr = '\n\n{0}\nusage: {1} INTEGER\n'.format(__desc__, argv[0])
try:
    random_bits = int(argv[1])
except IndexError:
    stderr.write('error: requires a number of bits to generate)' + commonerr)
    exit(1)
except ValueError:
    stderr.write('error: please enter a base 10 integer e.g. 256' + commonerr)
    exit(2)

# Thanks to http://stackoverflow.com/a/8734361
def base256_encode(n, minwidth=0): # int/long to byte array
    if n > 0:
        arr = []
        while n:
            n, rem = divmod(n, 256)
            arr.append(rem)
            b = bytearray(reversed(arr))
    elif n == 0:
        b = bytearray(b'\x00')
    else:
        raise ValueError

    if minwidth > 0 and len(b) < minwidth: # zero padding needed?
        b = (minwidth-len(b)) * '\x00' + b
    return b

generator = SystemRandom()
arr = base256_encode(generator.getrandbits(random_bits))
print(repr(bytes(arr)))
