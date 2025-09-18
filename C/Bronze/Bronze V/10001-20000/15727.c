#include <stdio.h>

int main() {
    int n, cnt = 0;
    scanf("%d", &n);

    while (n >= 5) {
        cnt++;
        n -= 5;
    }
    if (n) printf("%d", ++cnt);
    else printf("%d", cnt);
}