#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int *array;
  size_t used;
  size_t size;
} Array;

void initArray(Array *a, size_t initialSize) {
  // printf("initialSize: %zu\n", initialSize);
  a->array = (int *)malloc(initialSize * sizeof(int));
  a->used = 0;
  a->size = initialSize;
  // printf("a->used: %zu\n", a->used);
  // printf("a->size: %zu\n", a->size);
}

void insertArray(Array *a, int element) {
  // a->used is the number of used entries, because a->array[a->used++] updates a->used only *after* the array has been accessed.
  // Therefore a->used can go up to a->size
  // printf("inserting element: %d\n", element); 
  if (a->used == a->size) {
    a->size *= 2;
    a->array = (int *)realloc(a->array, a->size * sizeof(int));
  }
  a->array[a->used++] = element;
  // printf("a->used: %zu\n", a->used);
  // printf("a->size: %zu\n", a->size);
}

void removeArray(Array *a, Array *b, int element) {
  // // a->used is the number of used entries, because a->array[a->used++] updates a->used only *after* the array has been accessed.
  // // Therefore a->used can go up to a->size
  printf("removing element: %d\n", element); 
  // if (a->used == a->size) {
  //   a->size *= 2;
  //   a->array = (int *)realloc(a->array, a->size * sizeof(int));
  // }
  // a->array[a->used++] = element;
  // printf("a->used: %zu\n", a->used);
  // printf("a->size: %zu\n", a->size);

  initArray(b, a->size - 1);
  for (int i=0; i<a->size; ++i) {
    // printf("---%d\n", i);
    // printf("------%d\n", a->array[i]);

    if (a->array[i] != element) {
      b->array[b->used++] = a->array[i];
    }
  }

  // for (int i=0; i<b->size; ++i) {
  //   printf("---%d\n", i);
  //   printf("------%d\n", b->array[i]);
  // }
  // printf("b->size: %zu\n", b->size);
  // return b;
}

void freeArray(Array *a) {
  free(a->array);
  a->array = NULL;
  a->used = a->size = 0;
}

// Array mergeSort(Array a) {
//   Array a1, a2;
//   int a1_len, a2_len;
//   int len = a.size;

//   if (len == 1) {
//     return a;
//   }

//   if (len % 2 == 1) {
//     a1_len = len / 2;
//     a2_len = len / 2 + 1;

//   } else {
//     a1_len = a2_len = len / 2;
//     initArray(&a1, a1_len);
//     initArray(&a2, a2_len);
//     for (int i=0; i<len; ++i) {
//       if (i >= len / 2) {
//         insertArray(&a2, a.array[i]);
//       } else
//         insertArray(&a1, a.array[i]);
//     }
//   }

//   Array l = mergeSort(a1);
//   Array r = mergeSort(a2);

//   return merge(l, r);
// }

// Array merge(Array l, Array, r) {
//       c = []

//     while l and r:
//         if l[0] > r[0]:
//             c.append(r[0])
//             r.remove(r[0])
//         else:
//             c.append(l[0])
//             l.remove(l[0])

//     while a:
//         c.append(l[0])
//         l.remove(l[0])

//     while r:
//         c.append(r[0])
//         r.remove(r[0])

//     return c
// /////////////////////
//   Array c;

//   while (l.size != 0 && r.size != 0) {
//     if (l.array[0] > r.array[0]) {
//       insertArray(&c, r.array[0]);

//     }
//   }
// }


int main(int argc, char* argv[]) {

  Array a, b;
  initArray(&a, 12);
  initArray(&b, 11);
  for (int i=12; i>0; --i) { printf("inserting: %d\n", i); insertArray(&a, i); }
  // for (int i=1; i<13; ++i) { printf("%d\n", a.array[i-1]); }

  printf("a.used: %zu\n", a.used);
  printf("a.size: %zu\n", a.size);
  for (int i=1; i<=a.size; ++i) { printf("%d: %d\n", i, a.array[i-1]); }
  
  removeArray(&a, &b, 6);
  freeArray(&a);

  printf("b.used: %zu\n", b.used);
  printf("b.size: %zu\n", b.size);
  for (int i=1; i<=b.size; ++i) { printf("%d\n", b.array[i-1]); }
  // freeArray(&a);
  // for (int i=1; i<13; ++i) { printf("%d\n", b->array[i-1]); }

  freeArray(&b);
}

// int main() {

// }