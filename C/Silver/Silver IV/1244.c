#include <stdio.h>

int main() {
    int n;
    int arr[101];
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    int st;
    int gen, num;
    int left = 0, right = 0;
    scanf("%d", &st);

    for (int i=0; i<st; i++) {
        scanf("%d %d", &gen, &num);

        // 남학생일때    
        if (gen == 1) {
            for (int j=num; j<=n; j+=num) {
                if (arr[j-1]) arr[j-1] = 0;
                else arr[j-1] = 1;
            }
        }
        // 여학생일때
        else if (gen == 2) {
            int left = num - 1;
            int right = num - 1;

            while (left > 0 && right < n - 1) {
                if (arr[left - 1] != arr[right + 1]) break;
                left--;
                right++;
            }

            for (int j = left; j <= right; j++) {
                if (arr[j]) arr[j] = 0;
                else arr[j] = 1;
            }
        }

        // for (int i=0; i<n; i++) {
        //     printf("%d ", arr[i]);
        // }
        // printf("\n\n");
    }
    int idx = 0;
    while (n > 0) {
        if (n < 20) {
            for (int i=0; i<n; i++) {
                printf("%d ", arr[i+idx]);
            }
            printf("\n");
            n = 0;
        }
        else {
            for (int i=0; i<20; i++) {
                printf("%d ", arr[i+idx]);
            }
            printf("\n");
            n -= 20;
            idx += 20;
        }
    }
}