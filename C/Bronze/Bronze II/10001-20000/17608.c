#include <stdio.h>

int main() {
    int n, cnt = 1;
    int arr[100001];
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    int seeing = arr[n-1];

    for (int i=n-1; i>=0; i--) {
        if (arr[i] > seeing) {
            cnt += 1;
            seeing = arr[i];
        }
    }

    printf("%d", cnt);
}