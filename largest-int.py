'''
Write a program to determine the largest possible integer using the same number of 1 bits in a given number.
'''

import sys

arg = int(sys.argv[1])

def intToBin(k):
  if k == 0: return 0
  if k == 1: return 1
  return (k % 2) + 10 * intToBin(k / 2)

def oneBits(k, count = 0):
    s = str(intToBin(k))
    for c in s:
        if c == '1': count += 1
    return count

def binToInt(s, n = 0, j = 0):
    for i in reversed(range(0, len(s))):
        n += int(s[j]) * (2**i)
        j += 1
    return n

def maxBin(s, m = ''):
    itob = intToBin(s)
    count = oneBits(s)
    for i in range(0, count):
        m += '1'
    for i in range(count, len(str(itob))):
        m += '0'
    return m

print str(arg) + " -> " + str(intToBin(arg))
print "maxBin(" + str(intToBin(arg)) + ") -> " + str(maxBin(arg))
print maxBin(arg) + " -> " + str(binToInt(str(maxBin(arg))))