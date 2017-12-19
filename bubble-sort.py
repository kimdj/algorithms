'''
Bubble Sort.
'''

from test import *

count = 0

def bubbleSort(a):
    global count
    j = 0
    while True:
        swapped = False
        for i in range(0, len(a)-j-1):
            if a[i] > a[i+1]:
                count += 1
                a[i],a[i+1] = a[i+1],a[i]
                swapped = True
        if swapped == False:
            break
        j += 1

def bubbleSort2(alist):
    global count
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                count += 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

# bubbleSort(a)
# print a
# print "count: " + str(count)

bubbleSort2(a)
print a
print "count: " + str(count)