'''
Write a program to print the binary representation of an integer.
'''

import sys

arg = int(sys.argv[1])

def intToBin(k):
  if k == 0: return 0
  if k == 1: return 1
  return (k % 2) + 10 * intToBin(k / 2)

def intToBin_1(k):
    return k if k == 0 or k == 1 else ((k % 2) + 10 * intToBin_1(k / 2))

print intToBin(arg)
print intToBin_1(arg)