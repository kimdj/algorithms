'''
Write a program to print out the number of 1 bits in a given integer.
'''

import sys

arg = int(sys.argv[1])

def intToBin(k):
  if k == 0: return 0
  if k == 1: return 1
  return (k % 2) + 10 * intToBin(k / 2)

def oneBits(k):
    s = str(intToBin(k))
    count = 0
    for c in s:
        print c
        if c == '1': count += 1
    return count

print str(arg) + " -> " + str(intToBin(arg))
print "# of 1 bits:", oneBits(arg)