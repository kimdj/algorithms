import sys

# Recursive method
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-2) + fib(n-1)

# Iterative method
def fibIter(n, a = 0, b = 1, c = 0, count = 0):
    if n == 0:
        return 0
    while True:
        c = a + b
        a = b
        b = c
        # print a,
        count += 1
        if count == n:
            break
    return a

# Bottom-up method
def fibList(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# Memoization method
def fibMemo(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fibMemo(n-1, computed) + fibMemo(n-2, computed)
    return computed[n]

# userInput = input("How many Fibonnaci numbers would you like to generate? ")
userInput = int(sys.argv[1])

# print fib(userInput)
# print fibIter(userInput)
print fibList(userInput)[userInput]
print fibMemo(userInput)