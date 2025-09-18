#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int t=0; t<T; t++) {
        int a, b, c;
        int min, max;
        scanf("%d %d", &a, &b);

        if (a >= b) c = a;
        else c = b;

        for (int i=c; i>=1; i--) {
            for (int j=1; j<=c; j++) {
                if (a * i ==  b * j) {
                    min = a * i;
                    break;
                }
            }
        }
        
        for (int i=c; i>=1; i--) {
            if (a%i == 0 && b%i==0) {
                max = i;
                break;
            }
        }

        printf("%d %d\n", min, max);
    }
    return 0;
}