#include <stdio.h>
//should print 10
int mult(int a, int b){
    int result = a * b;
    return result;
}

int main(){
    int test = mult(5, 2);
    printf("%d", test);
    return 0;
}