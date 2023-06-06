#include <stdio.h>

// Should print the number 1

void f(int* a){
	(*a)++;
}

int main(){
	int x = 0;
	int* xp = &x;
	f(xp);
	printf("%d\n", *xp);

	return 1;
}
