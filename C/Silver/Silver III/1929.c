#include <stdio.h>
#include <math.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    for (int i=n; i<=m; i++) {
        if (i < 2) continue;

        int flag = 1;
        
        for (int j=2; j*j<=i; j++) {
            if (i % j == 0) {
                flag = 0;
                break;
            }
        }

        if (flag) printf("%d\n", i);
    }

    return 0;
}