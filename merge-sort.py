import sys
from test import *

'''
Create a new empty list, A.
Insert each least item from L and R lists into A.
Then, L or R will be empty while the other list
will contain items that are already sorted.
Insert the remaining sorted items into A.
'''
def merge(L,R):
    A = []                          # Create an empty list.

    #        L     R          A
    # e.g. [4,5] [3,6]  -->  [ ]

    while L and R:                  # While L and R are not empty,
        if L[0] > R[0]:             # insert items into the list by order.
            A.append(R[0])
            R.remove(R[0])
        else:
            A.append(L[0])
            L.remove(L[0])

    #       L   R           A
    # e.g. [ ] [6]  -->  [3,4,5]

    while L:                        # Either L or R contains remaining sorted items.
        A.append(L[0])              # Insert the remaining sorted items.
        L.remove(L[0])
    while R:
        A.append(R[0])
        R.remove(R[0])

    #       L   R            A
    # e.g. [ ] [ ]  -->  [3,4,5,6]

    return A

def mergeSort(A):
    if len(A) <= 1:                             # Base case: a list only contains a single item.
        return A
    
    L = mergeSort(A[0:len(A)/2])                # Keep recursively dividing the list until the base
    R = mergeSort(A[len(A)/2:len(A)])           # case is reached (i.e. a list contains only 1 item).

    return merge(L,R)

'''-------------------------------------------------------------------------------------------------'''

try: a
except NameError: a = None

if len(sys.argv) > 1:
    a = []
    for i in xrange(1, len(sys.argv)):
        a.append(int(sys.argv[i]))
elif a is None:
    a = [5,4,6,3,7,2,8,1,9]

print "unsorted a: " + str(a)
print "  sorted a: " + str(mergeSort(a))

'''================================================================================================='''

# '''
# Merge Sort.
# '''

# import sys
# from test import *

# def merge(l, r):
#     c = []

#     while l and r:
#         if l[0] > r[0]:
#             c.append(r[0])
#             r.remove(r[0])
#         else:
#             c.append(l[0])
#             l.remove(l[0])

#     # Now, l or r is empty.

#     while l:
#         c.append(l[0])
#         l.remove(l[0])
#     while r:
#         c.append(r[0])
#         r.remove(r[0])

#     return c

# def mergeSort(a):
#     n = len(a)
#     if n == 1:
#         return a

#     l = a[0:n/2]
#     r = a[n/2:n]

#     l = mergeSort(l)
#     r = mergeSort(r)

#     return merge(l, r)

# b = mergeSort(a)
# print b

# '''================================================================================================='''

# # Python program for implementation of MergeSort
 
# # Merges two subarrays of arr[].
# # First subarray is arr[l..m]
# # Second subarray is arr[m+1..r]
# def merge2(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r- m
 
#     # create temp arrays
#     L = [0] * (n1)
#     R = [0] * (n2)
 
#     # Copy data to temp arrays L[] and R[]
#     for i in range(0 , n1):
#         L[i] = arr[l + i]
 
#     for j in range(0 , n2):
#         R[j] = arr[m + 1 + j]
 
#     # Merge the temp arrays back into arr[l..r]
#     i = 0     # Initial index of first subarray
#     j = 0     # Initial index of second subarray
#     k = l     # Initial index of merged subarray
 
#     while i < n1 and j < n2 :
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
 
#     # Copy the remaining elements of L[], if there
#     # are any
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
 
#     # Copy the remaining elements of R[], if there
#     # are any
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
 
# # l is for left index and r is right index of the
# # sub-array of arr to be sorted
# def mergeSort2(arr,l,r):
#     if l < r:
 
#         # Same as (l+r)/2, but avoids overflow for
#         # large l and h
#         m = (l+(r-1))/2
 
#         # Sort first and second halves
#         mergeSort2(arr, l, m)
#         mergeSort2(arr, m+1, r)
#         merge2(arr, l, m, r)
 
 
# # # Driver code to test above
# # # arr = [12, 11, 13, 5, 6, 7]
# # arr = a
# # n = len(arr)
# # print ("Given array is")
# # for i in range(n):
# #     print ("%d" %arr[i]),
 
# # mergeSort2(arr,0,n-1)
# # print ("\n\nSorted array is")
# # for i in range(n):
# #     print ("%d" %arr[i]),
