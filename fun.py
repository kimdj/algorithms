import sys
import random
from time import sleep

# arg = int(sys.argv[1])

def intToBin(k):
  if k == 0: return k
  if k == 1: return k
  return (k % 2) + 10 * intToBin(k / 2)

def intToBin_1(k):
    return k if k == 0 or k == 1 else ((k % 2) + 10 * intToBin_1(k / 2))

while True:
  rand = random.randint(1,999999),
  # print rand[0]
  if rand[0] == 1:
      print "FOUND!"
      break
  # print intToBin(rand)
  # print intToBin_1(rand)
  # sleep(1) # Time in seconds.