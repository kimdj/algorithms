'''
Heap Sort Implementation.
'''
import sys
from test import *

def wait(msg):
    try:
        input(msg)
    except SyntaxError:
        pass

def heapify(A, n, i):

    '''
            A
       [5,4,3,2,1]
    '''

    largest = i         # Initialize largest as root
    l = 2 * i + 1       # left = 2*i + 1
    r = 2 * i + 2       # right = 2*i + 2
 
    # # See if left child of root exists and is
    # # greater than root
    # if l < n and A[i] < A[l]:
    #     largest = l
 
    # # See if right child of root exists and is
    # # greater than root
    # if r < n and A[largest] < A[r]:
    #     largest = r

    # See if left child of root exists and is
    # greater than root
    if r < n and A[i] < A[r]:
        largest = r

    # See if right child of root exists and is
    # greater than root
    if l < n and A[largest] < A[l]:
        largest = l

    # Change root, if needed
    if largest != i:
        print "SWAPPING " + str(A[i]) + " <-> " + str(A[largest])
        A[i],A[largest] = A[largest],A[i]  # swap
 
        # Heapify the root.
        heapify(A, n, largest)
 
# The main function to sort an array of given size
def heapSort(A):
    n = len(A)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(A, n, i)
        print A

    print "---------"

    # One by one extract elements
    for i in range(n-1, 0, -1):
        print A
        A[i], A[0] = A[0], A[i]   # swap
        heapify(A, i, 0)

    return A

'''-------------------------------------------------------------------------------------------------'''

try: a
except NameError: a = None

if len(sys.argv) > 1:
    a = []
    for i in xrange(1, len(sys.argv)):
        a.append(sys.argv[i])
elif a is None:
    a = [12,11,13,5,6,7,1,4,2,3,9,8,10]

print "unsorted a: " + str(a)
heapSort(a)
print "  sorted a: " + str(a)

'''================================================================================================='''

# import sys
# from test import *

# def wait(msg):
#     try:
#         input(msg)
#     except SyntaxError:
#         pass

# # To heapify subtree rooted at index i.
# # n is size of heap
# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1     # left = 2*i + 1
#     r = 2 * i + 2     # right = 2*i + 2
 
#     # See if left child of root exists and is
#     # greater than root
#     if l < n and arr[i] < arr[l]:
#         largest = l
 
#     # See if right child of root exists and is
#     # greater than root
#     if r < n and arr[largest] < arr[r]:
#         largest = r
 
#     # Change root, if needed
#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
#         # Heapify the root.
#         heapify(arr, n, largest)
 
# # The main function to sort an array of given size
# def heapSort(A):
#     arr = A[:]          # Copy the list by slicing.
#     # arr = list(A)       # Or by using the built-in list(). [Note: also consider copy.copy(), copy.deepcopy()]
#     n = len(arr)

#     # Build a maxheap.
#     for i in range(n, -1, -1):
#         heapify(arr, n, i)

#     # One by one extract elements
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]   # swap
#         heapify(arr, i, 0)

#     return arr

# # # Driver code to test above
# # arr = [12, 11, 13, 5, 6, 7]
# # print "unsorted arr: " + str(arr)
# # heapSort(arr)
# # n = len(arr)
# # print "Sorted array is:", arr
# # # for i in range(n):
# # #     print ("%d" %arr[i]),

# '''-------------------------------------------------------------------------------------------------'''

# try: a
# except NameError: a = None

# if len(sys.argv) > 1:
#     a = []
#     for i in xrange(1, len(sys.argv)):
#         a.append(sys.argv[i])
# elif a is None:
#     a = [12,11,13,5,6,7,1,4,2,3,9,8,10]

# print "unsorted a: " + str(a)
# b = heapSort(a)
# print "  sorted b: " + str(b)

'''================================================================================================='''

# # Python program for implementation of heap Sort
 
# # To heapify subtree rooted at index i.
# # n is size of heap
# def heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1     # left = 2*i + 1
#     r = 2 * i + 2     # right = 2*i + 2
 
#     # See if left child of root exists and is
#     # greater than root
#     if l < n and arr[i] < arr[l]:
#         largest = l
 
#     # See if right child of root exists and is
#     # greater than root
#     if r < n and arr[largest] < arr[r]:
#         largest = r
 
#     # Change root, if needed
#     if largest != i:
#         arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
#         # Heapify the root.
#         heapify(arr, n, largest)
 
# # The main function to sort an array of given size
# def heapSort(arr):
#     n = len(arr)
 
#     # Build a maxheap.
#     for i in range(n, -1, -1):
#         heapify(arr, n, i)
 
#     # One by one extract elements
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]   # swap
#         heapify(arr, i, 0)
 
# # Driver code to test above
# arr = [12, 11, 13, 5, 6, 7]
# print "unsorted arr: " + str(arr)
# heapSort(arr)
# n = len(arr)
# print "Sorted array is:", arr
# # for i in range(n):
# #     print ("%d" %arr[i]),
# # This code is contributed by Mohit Kumra