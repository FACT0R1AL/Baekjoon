#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int i=0; i<T; i++) {
        int q=0, d=0, n=0, p=0;
        int c;
        scanf("%d", &c);

        q = c/25;
        c = c%25;
        d = c/10;
        c = c%10;
        n = c/5;
        c = c%5;
        p = c;
        printf("%d %d %d %d\n", q, d, n, p);
    }
    return 0;
}