#include <stdio.h>

int main() {
    int n, temp;
    int arr[100000][2];
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        for (int j=0; j<2; j++)
            scanf("%d", &arr[i][j]);
    }
}