import sys
import getopt


def convert(char, type):
    if type == 'encode':
        ascii = ord(char)
        if char.isupper():
            ascii += 13
            if ascii > 90:
                ascii -= 26
        else:
            ascii += 13
            if ascii > 122:
                ascii -= 26
        return chr(ascii)
    else:
        ascii = ord(char)
        if char.isupper():
            ascii -= 13
            if ascii < 65:
                ascii += 26
        else:
            ascii -= 13
            if ascii < 97:
                ascii += 26
        return chr(ascii)


def encode(str):
    tmp = ''
    for i in str:
        if i.isalpha():
            tmp += convert(i, 'encode')
        else:
            tmp += i
    return tmp


def decode(str):
    tmp = ''
    for i in str:
        if i.isalpha():
            tmp += convert(i, 'decode')
        else:
            tmp += i
    return tmp


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ed')
        if len(opts) != 1:
            print 'wrong options.'
            exit()
        if opts[0][0] == '-e':
            origin_str = raw_input()
            print encode(origin_str)
            exit()
        if opts[0][0] == '-d':
            origin_str = raw_input()
            print decode(origin_str)
            exit()
    except getopt.GetoptError, e:
        print e
