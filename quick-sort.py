'''
Quick Sort.
'''
from test import *

def quickSort(A, lo, hi):
    if lo < hi:
        pivot = partition(A, lo, hi)
        quickSort(A, lo, pivot)
        quickSort(A, pivot+1, hi)
    return a

def partition(A, lo, hi):
    pivot = A[lo]
    leftwall = lo
    for i in xrange(lo+1, hi):
        if A[i] < pivot:
            A[i], A[leftwall] = A[leftwall], A[i]     # swap
            leftwall += 1
    pivot, A[leftwall] = A[leftwall], pivot           # swap
    return leftwall

a = [6,3,4,1,5,2]
b = a[:]
quickSort(b, 0, len(b))
print a
print b

'''---------------------------------------------------------------------------------------------------'''

# import random

# def display(A):
#     print A

# def swap(A, i, j):
#     print "SWAPPING: " + str(A[i]) + " <-> " + str(A[j])
#     A[i],A[j] = A[j],A[i]

# def partition():
#     return

# def quickSort(A):
#     display(A)
#     print
#     n = len(A)

#     # Choose a random pivot.
#     pivot = random.randint(0,n-1)
#     # pivot = 3
#     print "pivot: " + str(pivot)
#     print "pivot value: " + str(A[pivot])

#     # Move pivot to the end of the list.
#     swap(A, pivot, n-1)
#     print

#     i = 0
#     j = n-2

#     # Choose L. (larger than pivot)
#     # Choose R. (smaller than pivot)
#     while i < j:
#         display(A)
#         L, R = 0, 0

#         while A[i] < A[n-1]:
#             i += 1
#             if A[i] > A[n-1]:
#                 L = i
#                 print "foo"

#         while A[j] > A[n-1] and j > i:
#             j -= 1
#             if A[j] < A[n-1]:
#                 R = j
#                 print "bar"

#         if i == j:
#             R = None

#         print "i:", i, "  ", "A[i]:", A[i]
#         print "j:", j, "  ", "A[j]:", A[j]

#         print A[i], "is larger than", A[n-1]
#         print A[j], "is smaller than", A[n-1]

#         if R is not None:
#             swap(A, i, j)
#             display(A)

#             i += 1
#             j -= 1
#             x = raw_input()
#         else:
#             swap(A, i, n-1)
#             display(A)

#     # Now, swap pivot with itemFromLeft.
#     swap(A, i, n-1)
#     print "SWAPPING: " + str(A[i]) + " <-> " + str(A[n-1])

#     print "\n----------------------\n"

#     quickSort(A[0:pivot])
#     quickSort(A[pivot+1, n-1])

#     display(A)







# a = [2,6,5,3,8,7,1,0]

# quickSort(a)

'''---------------------------------------------------------------------------------------------------'''

# from test import *

# def wait():
#     try:
#         input("Press enter to continue")
#     except SyntaxError:
#         pass

# def quickSort(a, lo, hi):
#     if lo < hi:
#         pivot = partition(a, lo, hi)
#         quickSort(a, lo, pivot)
#         quickSort(a, pivot+1, hi)
#     return a

# def partition(a, lo, hi):
#     pivot = a[lo]
#     leftwall = lo

#     for i in xrange(lo+1, hi):
#         print "--------------------- a[" + str(i) + "]: " + str(a[i])
#         print "array: " + str(a)
#         print "leftwall: " + str(leftwall)
#         print "rightwall (i): " + str(i)
#         print "pivot: " + str(pivot)
#         if a[i] < pivot:
#             print "swapping " + str(a[i]) + " <-> " + str(a[leftwall])
#             a[i], a[leftwall] = a[leftwall], a[i]     # swap
#             leftwall += 1
#         wait()

#     pivot, a[leftwall] = a[leftwall], pivot           # swap

#     return leftwall

# a = [6,3,4,1,5,2]

# b = quickSort(a, 0, len(a))
# print b