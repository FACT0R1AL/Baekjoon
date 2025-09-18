#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int i=0; i<T; i++) {
        int cnt = 0;
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);

        for (int x=1; x<=a; x++) {
            for (int y=1; y<=b; y++) {
                for (int z=1; z<=c; z++) {
                    if (((x % y) == (y % z)) && ((y % z) == (z % x)) && ((x % y) == (x % z))) {
                        cnt += 1;
                    }
                }
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}