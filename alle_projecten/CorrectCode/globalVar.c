#include <stdio.h>

int x = 10;
//should print 10, 20, 30
int main(){
    printf("%d", x);
    int x = 20;
    printf("%d", x);
    if (x == 20){
        int x = 30;
        printf("d", x);
    }
    return 1;
}