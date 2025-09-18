#include <stdio.h>

int main() {
    int n, fib2[1000] = {0};
    scanf("%d", &n);
    fib2[0] = 1;
    fib2[1] = 3;

    for (int i=2; i<=n; i++) {
        fib2[i] = (fib2[i-1] + 2*fib2[i-2])%10007;
    }

    printf("%d", fib2[n-1]);
    return 0;
}