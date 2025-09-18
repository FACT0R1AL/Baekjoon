#include <stdio.h>

int main() {
    int n, f;
    scanf("%d", &n);
    scanf("%d", &f);

    int n2 = n - (n % 100);
    int min = 0;

    for (int i=99; i>=0; i--) {
        if ((n2+i) % f == 0) {
            min = i;
        }
    }

    if (min < 10) {
        printf("0%d", min);
    }
    else {
        printf("%d", min);
    }

    return 0;
}