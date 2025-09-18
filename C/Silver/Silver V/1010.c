#include <stdio.h>

long long int comb(int n, int r) {
    if (r > n - r) r = n - r; // 대칭성 이용
    long long result = 1;
    for (int i = 1; i <= r; i++) {
        result = result * (n - r + i) / i;
    }
    return result;
}

int main() {
    int n;
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        long long int a, b;
        scanf("%lld %lld", &a, &b);

        long long int result = comb(b, a);

        printf("%lld\n", result);
    }
}