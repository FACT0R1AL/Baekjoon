#include <stdio.h>

int main() {
    int arr[101];

    for (int i=0; i<5; i++) {
        scanf("%d", &arr[i]);
    }
    
    int i = 1;

    while (1) {
        int cnt = 0;

        for (int j=0; j<5; j++) {
            if (i % arr[j] == 0) {
                cnt++;
            }
        }

        if (cnt >= 3) {
            printf("%d", i); break;
        }
        
        i++;
    }
}