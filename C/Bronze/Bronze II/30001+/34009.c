#include <stdio.h>

int main() {
    int n;
    int arr[100001];
    
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    if (n%2) printf("Bob");
    else printf("Alice");
}