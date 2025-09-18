#include <stdio.h>

int main() {
    int n, arr[50000], sum = 0;
    int x = 0;
    int min = 50000000;
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    for (int i=0; i<n; i++) {
        x = sum - arr[i];
        if (x < min) min = x;
    }

    printf("%d", min);
    
    return 0;
}