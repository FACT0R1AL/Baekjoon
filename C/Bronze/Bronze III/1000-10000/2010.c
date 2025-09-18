#include <stdio.h>

int main() {
    int n;
    int sum = 0;
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        int a;
        scanf("%d", &a);

        if (i) sum += a-1;
        else sum += a;
    }

    printf("%d", sum);
}