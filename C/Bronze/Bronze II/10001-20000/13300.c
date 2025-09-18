#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;
    int k, x;
    int cnt = 0;

    scanf("%d %d", &a, &b);
    scanf("%d %d", &k, &x);

    for (int i=a; i<=b; i++) {
        if (i <= k+x && i >= k-x) cnt++;
    }

    if (!cnt) printf("IMPOSSIBLE");
    else printf("%d", cnt);
}