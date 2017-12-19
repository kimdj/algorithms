'''
Quick Sort.
'''

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
        if a[i] < pivot:
            a[i], a[leftwall] = a[leftwall], a[i]
            leftwall = leftwall + 1

    pivot, a[leftwall] = a[leftwall], pivot

    return leftwall

a = [6, 5, 4, 3, 2, 1]

b = quickSort(a, 0, 6)
print b