#include <stdio.h>

// Should print the numbers 1 - 5
int main(){
	int a = 5;
	int* b = &a;
	(*b)++;
}
