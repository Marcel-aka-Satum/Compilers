int main(){
    int c = 5;
    int* b = &c;
    int** x = &b;
    int*** a = &x;
    int d = **a;
}