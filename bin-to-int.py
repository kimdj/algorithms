'''
Write a program to print the integer representation of an binary.
'''

import sys

arg = int(sys.argv[1])

def binToInt(s, n = 0, j = 0):
    for i in reversed(range(0, len(s))):
        n += int(s[j]) * (2**i)
        j += 1
    return n

print str(arg) + " -> " + str(binToInt(str(arg)))