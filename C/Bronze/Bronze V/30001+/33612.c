#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    int res = 2024*12 + 8 + (n-1)*7;
    if (res % 12 == 0) printf("%d %d", res/12-1, 12);
    else printf("%d %d", res/12, res%12);
}