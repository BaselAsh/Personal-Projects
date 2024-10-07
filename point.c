#include <stdio.h>
#include <stdlib.h>

int main(void){
    int *n;
    n = malloc(sizeof(int));
    printf("What's N: ");
    scanf("%i", &n);
    printf("The int is (%i)\n", n);
}