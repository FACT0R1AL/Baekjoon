#include <stdio.h>

int hap(int n, int k) {
    int m = n / k;
    return k * m * (m + 1) / 2;
}
int main() {
    int n;
    scanf("%d", &n);
    
    int arr[n];
    
    for (int i=0; i<n; i++) {
        int sum = 0;
        scanf("%d", &arr[i]);
        
        sum = hap(arr[i], 3) + hap(arr[i], 7) - hap(arr[i], 21);

        printf("%d\n", sum);
    }
}