#include <stdio.h>

int main() {
    char a[4], b[4];
    scanf("%s %s", a, b);
    
    int temp = a[2];
    a[2] = a[0];
    a[0] = temp;

    temp = b[2];
    b[2] = b[0];
    b[0] = temp;
    
    int ant = (a[0] - '0')*100 + (a[1] - '0')*10 + (a[2] - '0');
    int bnt = (b[0] - '0')*100 + (b[1] - '0')*10 + (b[2] - '0');

    (ant > bnt) ? printf("%d", ant) : printf("%d", bnt);
}