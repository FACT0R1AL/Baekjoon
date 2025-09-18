#include <stdio.h>

int main() {
    int n, arr[10];
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    for (int i=0; i<n; i++) {
        if (arr[i] == 0 || arr[i] == 1) printf("1\n");
        else if (arr[i] == 2) printf("2\n");
        else if (arr[i] == 3) printf("6\n");
        else if (arr[i] == 4) printf("4\n");
        else printf("0\n");
    }
    return 0;
}