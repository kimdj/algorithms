a = [[], [1, 2, 3], [4, 5], [], [], [6, 7], [8], [9, 10], [], []]
b = []

for array in a:
    for item in array:
        b.append(item)

for item in b:
    if item == b[len(b) - 1]:
        print str(item)
    else:
        print str(item) + ',',