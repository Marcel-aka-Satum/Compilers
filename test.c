#include <stdio.h>

/*
This should print the numbers: 9,-9,9,-9
*/
int main(){
	printf("%d; ", -(-9));
	printf("%d; ", -(+9));
	printf("%d; ", +9);
	printf("%d; ", -9);
    return 1;
}
