#include <stdio.h>

int main() {
    int n, abc[3];
    int sum[3] = {0,}, sumsqr[3] = {0,};
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        for (int j=0; j<3; j++)
            scanf("%d", &abc[j]);

        for (int j=0; j<3; j++) {
            sum[j] += abc[j];
            sumsqr[j] += abc[j] * abc[j];
        }
    }

    if (sumsqr[0] > sumsqr[1] && sumsqr[0] > sumsqr[2]) printf("1 %d", sum[0]);
    
    else if (sumsqr[1] > sumsqr[0] && sumsqr[1] > sumsqr[2]) printf("2 %d", sum[1]);
    
    else if (sumsqr[2] > sumsqr[0] && sumsqr[2] > sumsqr[1]) printf("3 %d", sum[2]);

    else {
        int max = sum[0];
        for (int i=0; i<3; i++) {
            if (sum[i] > max) max = sum[i];
        }

        printf("0 %d", max);
    }

    return 0;
}