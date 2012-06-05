from sys import version_info, getsizeof
import re

if (version_info[0] <= 2):
    bytes = str
    str = unicode
    def divide(num, dem):
        return float(num) / dem
else:
    def divide(num, dem):
        return num / dem

def string_memory(string, encoding='utf-8'):
    if isinstance(string, str):
        size_str = getsizeof(string)
        size_bytes = getsizeof(string.encode(encoding))
    elif isinstance(string, bytes):
        size_str = getsizeof(string.decode(encoding))
        size_bytes = getsizeof(string)

    size_total = size_str + size_bytes
    size_diff = size_str - size_bytes
    size_over = divide(size_str, size_bytes)
    size_under = divide(size_bytes, size_str)

    size_dict = {'input': string, 'str': size_str, 'bytes': size_bytes, 'total': size_total, 'diff': size_diff}
    if size_over > size_under:
        size_dict['bigger'] = 'Unicode'
        size_dict['smaller'] = 'bytes'
        size_dict['over'] = size_over
        size_dict['under'] = size_under
    else:
        size_dict['bigger'] = 'bytes'
        size_dict['smaller'] = 'Unicode'
        size_dict['over'] = size_under
        size_dict['under'] = size_over
    return size_dict

if __name__ == '__main__':
    from sys import argv, stdin
    arg = ' '.join(argv[1:])
    if arg == '':
        raise ValueError('need a string')

    size_dict = string_memory(arg, stdin.encoding)

    print('''
    Input string: %s\n
    Size of Unicode string: %d bytes
    Size of byte string: %d bytes
    Total size: %d bytes
    Difference between sizes (negative means Unicode is smaller): %d bytes
    Percent %s is bigger than %s: %.2f%%
    Percent %s is smaller than %s: %.2f%%
    ''' % (
        size_dict['input'],
        size_dict['str'],
        size_dict['bytes'],
        size_dict['total'],
        size_dict['diff'],
        size_dict['bigger'],
        size_dict['smaller'],
        size_dict['over']*100,
        size_dict['smaller'],
        size_dict['bigger'],
        size_dict['under']*100,
        )
    )
