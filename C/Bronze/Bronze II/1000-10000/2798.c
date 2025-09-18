#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, m;
    int arr[100];
    int min = 300000;

    scanf("%d %d", &n, &m);

    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            for (int k=0; k<n; k++) {
                int sum;
                if (i != j && j != k && i != k) sum = arr[i]+arr[j]+arr[k];
                if (abs(min) > abs(sum - m) && m >= sum) min = sum-m;
            }
        }
    }

    printf("%d", min+m);
}