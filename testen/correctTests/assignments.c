int a = 3;
int c = 10;
int*** b = &c;
a = 6;
***b = a;
a = ***b;
