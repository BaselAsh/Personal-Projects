#include <stdio.h>
#include <stdlib.h>

void swap(int *x, int *y);

void main(void){
    int x = 1;
    int y = 2;
    printf("x = %i, y = %i\n", x, y);
    swap(&x, &y);
    printf("x = %i, y = %i\n", x, y);
}

void swap(int *x, int *y){
    int z = *x;
    *x = *y;
    *y = z;
}