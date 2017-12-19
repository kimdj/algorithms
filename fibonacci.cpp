#include <iostream>

using namespace std;

int fib(int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  }
  return fib(n-2) + fib(n-1);
}

int main(){
  for (int i=0; i<10; ++i) {
    int x = fib(i);
    printf("%d\n", x);
  }
}