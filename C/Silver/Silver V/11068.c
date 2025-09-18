#include <stdio.h>
#include <string.h>

int main() {
    int t;
    scanf("%d", &t);

    for (int i=0; i<t; i++) {
        int n;
        int arr[21] = {0,}, idx = 0;
        int flag = 1;
        scanf("%d", &n);

        for (int j=2; j<=64; j++) {
            idx = 0;
            flag = 1;
            int temp = n;

            while (temp >= j) {
                arr[idx++] = temp % j;
                temp /= j;
            }

            arr[idx++] = temp;
            
            for (int i=0; i<idx; i++) {
                if (arr[i] != arr[idx - i - 1]) {
                    flag = 0;
                    break;
                }
            }

            if (flag) {
                printf("1\n");
                break;
            }
        }

        if (!flag) {
            printf("0\n");
        }
    }
}