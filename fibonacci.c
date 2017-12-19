/*
Calculate the nth fibonacci number.
*/

#include "stdio.h"

int fib(int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  }
  return fib(n-2) + fib(n-1);
}

int fib1(int n) {
  return (n == 0 || n == 1 ? n : (fib1(n-2) + fib1(n-1)));
}

int fib2(int n) {
  if (n == 0) return 0;
  if (n == 1) return 1;
  return fib2(n-2) + fib2(n-1);
}

int main(){
  for (int i=0; i<10; ++i) {
    int x = fib(i);
    int y = fib1(i);
    int z = fib2(i);
    printf("%d %d %d\n", x, y, z);
  }
}