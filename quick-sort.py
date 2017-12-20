'''
Quick Sort.
'''

from test import *

def wait():
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass

def quickSort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        quickSort(a, low, pivot)
        quickSort(a, pivot+1, high)
    return a

def partition(a, low, high):
    pivot = a[low]
    leftwall = low

    for i in xrange(low+1, high):
        print "--------------------- a[" + str(i) + "]: " + str(a[i])
        print "array: " + str(a)
        print "leftwall: " + str(leftwall)
        print "pivot: " + str(pivot)
        if a[i] < pivot:
            print "swapping " + str(a[i]) + " <-> " + str(a[leftwall])
            a[i], a[leftwall] = a[leftwall], a[i]     # swap
            leftwall += 1
        wait()

    pivot, a[leftwall] = a[leftwall], pivot           # swap

    return leftwall

a = [6,3,4,1,5,2]

b = quickSort(a, 0, len(a))
print b