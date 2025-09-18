#include <stdio.h>
#include <stdbool.h>

int prime(int a) {
    if (a == 1) return false;
    if (a == 2) return true;
    
    for (int i=2; i<a; i++)  {
        if (!(a%i)) {
            return false;
        }
    }

    return true;
}

int main() {
    int n, cnt = 0, arr[100];
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
        if (prime(arr[i])) cnt += 1;
    }

    printf("%d", cnt);
    return 0;
}