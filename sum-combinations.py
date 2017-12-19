'''
Given a list of item prices, find all possible combinations of items that sum a particular value K.
'''

import sys
import itertools

def combinationSum(prices, l = [], K = int(sys.argv[1])):
    # K = int(sys.argv[1])  # Target value.

    for i in range(1, len(prices) + 1):                       # From 1 to the length of prices.
        # print list(itertools.combinations(prices, i))
        for t in list(itertools.combinations(prices, i)):     # For each combination with i-length tuple, find the sum.
            total = 0
            for item in t:
                total += item
            # print total
            if total == K:                                    # If the sum of a particular combination is equal
                # print t
                l.append(t)                                       # to K, add it to the return list.
    return l

print combinationSum([1, 2, 3, 4, 5, 6, 7, 8, 9])
x = combinationSum([1, 2, 3, 4, 5, 6, 7, 8, 9])
print len(x)
for i in range(1, len(x) + 1):
    print i