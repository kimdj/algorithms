import random
import sys

n = int(sys.argv[1])
x = random.sample(xrange(0, n), n)
print x
