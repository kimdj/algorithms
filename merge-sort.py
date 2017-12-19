'''
Merge Sort.
'''

import sys
from test import *

def merge(l, r):
    c = []

    while l and r:
        if l[0] > r[0]:
            c.append(r[0])
            r.remove(r[0])
        else:
            c.append(l[0])
            l.remove(l[0])

    # Now, l or r is empty.

    while l:
        c.append(l[0])
        l.remove(l[0])
    while r:
        c.append(r[0])
        r.remove(r[0])

    return c

def mergeSort(a):
    n = len(a)
    if n == 1:
        return a

    l = a[0:n/2]
    r = a[n/2:n]

    l = mergeSort(l)
    r = mergeSort(r)

    return merge(l, r)

b = mergeSort(a)
print b