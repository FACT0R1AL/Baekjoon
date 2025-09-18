#include <stdio.h>

int main() {
    for (int i=0; i<3; i++) {
        int arr[4] = {0,};
        int a = 0, b = 0;

        for (int j=0; j<4; j++) {
            scanf("%d", &arr[j]);

            if (arr[j] == 0) a += 1;
            else b += 1;

            if (a == 1 && b == 3) printf("A\n");
            else if (a == 2 && b == 2) printf("B\n");
            else if (a == 3 && b == 1) printf("C\n");
            else if (a == 4) printf("D\n");
            else if (b == 4) printf("E\n"); 
        }
    }
}