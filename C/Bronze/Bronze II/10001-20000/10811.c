#include <stdio.h>

int main() {
    int n, m, arr[100];
    scanf("%d %d", &n, &m);

    for (int x=0; x<100; x++) {
        arr[x] = x+1;
    }

    for (int x=0; x<m; x++) {
        int i,j;
        scanf("%d %d", &i, &j);

        for (int y=i-1; y<j-1; y++) {
            if (y < j+i-y-2) {
                int temp = arr[j+i-y-2];
                arr[j+i-y-2] = arr[y];
                arr[y] = temp;
            }
        }
    }

    for (int i=0; i<n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}