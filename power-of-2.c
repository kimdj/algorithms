/*
Verify that an integer is a power of 2.
*/

/*
This function is the equivalent of the Divide by Two algorithm.
Dividing a binary integer by 2 is the same as shifting it right one bit, and checking whether
a binary integer is odd is the same as checking if its least significant bit is 1.
*/

#include "stdio.h"

typedef int bool;
#define true 1;
#define false 0;

bool powerOf2(int x) {
  if ((x!=0) && !(x & (x-1))) {
    return true;
  } else {
    return false;
  }
}

int powerOf2_1(int x){
  return ((x!=0) && !(x & (x-1))) ? 1 : 0;
}

int main() {
  for (int i=0; i<999999999; ++i) {
    if (powerOf2(i)) {
      printf("%d ", i);
    }
    if (powerOf2_1(i)) {
      printf("%d\n", i);
    }
  }
}