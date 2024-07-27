#include <stdio.h>

void brick(void);

int main(void){
    int n = 10;
    for (int i = 0; i < n; i++){
        for (int o = 0;o < i+1;o++){
            brick();
        }
        if(i != n-1){
            printf("\n");
        }
    }
}

void brick(void){
    printf("#");
}