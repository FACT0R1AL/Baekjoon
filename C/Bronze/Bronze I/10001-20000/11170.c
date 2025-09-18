#include <stdio.h>

int main() {
    int t;
    int n, m;
    scanf("%d", &t);

    for (int i=0; i<t; i++) {
        int cnt = 0;
        scanf("%d %d", &n, &m);
        for (int j=m; j>=n; j--) {
            if (j == 0) cnt += 1;
            for (int k=j; k>=1; k--) {
                while (k >= 10) {
                    if (k % 10 == 0) {
                        cnt += 1;
                        printf("%d\n", k);
                        k /= 10;
                    }
                    else {
                        k /= 10;
                    }
                }
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}