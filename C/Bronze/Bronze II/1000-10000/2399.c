#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[10001];
    int n;
    long long int sum = 0;
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            sum += abs(arr[i]-arr[j]);
        }
    }

    printf("%lld", sum);
}