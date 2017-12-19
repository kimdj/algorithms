'''
Verify that an integer is a power of 2.
'''

'''
This function is the equivalent of the Divide by Two algorithm.
Dividing a binary integer by 2 is the same as shifting it right one bit, and checking whether
a binary integer is odd is the same as checking if its least significant bit is 1.
'''

import sys

arg = int(sys.argv[1])

def powerOf2(x):
    if ((x != 0) and not (x & (x - 1))):
        return True
    else:
        return False

def powerOf2_1(x):
    return True if ((x != 0) and not (x & (x - 1))) else False

print powerOf2(arg)
print powerOf2_1(arg)