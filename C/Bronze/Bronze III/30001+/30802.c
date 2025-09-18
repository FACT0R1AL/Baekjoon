#include <stdio.h>

int main() {
    int n, t, p, size[6], cnt = 0;

    scanf("%d", &n);
    for (int i=0; i<6; i++) {
        scanf("%d", &size[i]);
    }
    scanf("%d %d", &t, &p);

    for (int i=0; i<6; i++) {
        if (size[i] > 0) {
            cnt += (size[i]-1) / t + 1;
        }
    }
    printf("%d\n", cnt);
    printf("%d %d", n/p, n%p);
    return 0;
}