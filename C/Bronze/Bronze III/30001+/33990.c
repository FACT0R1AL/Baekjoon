#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, min = 2147483647;
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        int a,b,c;
        scanf("%d %d %d", &a, &b, &c);

        int sum = a+b+c;

        if (sum >= 512 && abs(min) > abs(sum-512)) {
            min = sum-512;
            // printf("%d\n", min);
        }
    }

    if (min < 0 || min == 2147483647) printf("-1");
    else printf("%d", min+512);
}