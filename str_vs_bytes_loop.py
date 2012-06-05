from str_vs_bytes import string_memory
from sys import argv, stdin
from hurry import filesize

def format_output(i, size_dict):
    output = 'At iteration %d with %s characters, the %s string is %.7f%% bigger which amounts to %d bytes.' % (
            i,
            len(test_string),
            size_dict['bigger'],
            size_dict['over']*100,
            size_dict['diff'],
            )
    return output

test_char = test_string = ' '.join(argv[1:])
if test_string == '':
    raise ValueError('need a string')

i = 1

size_dict = string_memory(test_string, stdin.encoding)
print(format_output(i, size_dict))

while size_dict['over'] > 0.1:
    i += 1
    test_string += test_char
    size_dict = string_memory(test_string, stdin.encoding)
    print(format_output(i, size_dict))

