#include <stdio.h>

int main() {
    int n;
    long long int fib[1000];
    scanf("%d", &n);
    fib[0] = 1;
    fib[1] = 2;

    for (int i=2; i<n; i++) {
        fib[i] = (fib[i-1] + fib[i-2])%10007;
    }

    long long int result = fib[n-1] % 10007;
    printf("%lld", result);
    return 0;
}