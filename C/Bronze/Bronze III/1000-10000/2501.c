#include <stdio.h>

int main() {
    int n, k, idx = 2;
    int arr[10000] = {0,};
    arr[1] = 1;
    scanf("%d %d", &n, &k);
    
    for (int i=2; i<=n; i++) {
        if (n % i == 0) {
            arr[idx] = i;
            idx++;
        }
    }

    printf("%d", arr[k]);
}