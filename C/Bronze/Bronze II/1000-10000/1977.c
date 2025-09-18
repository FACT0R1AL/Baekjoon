#include <stdio.h>
#include <math.h>

int main() {
    int a, b, min = 0, sum = 0;
    scanf("%d %d", &a, &b);

    for (int i=a; i<=b; i++) {
        if (sqrt(i) - (int)(sqrt(i)) == 0) {
            if (min == 0) min = i;
            sum += i;
        }
    }

    if (min == 0) printf("-1");
    else printf("%d\n%d", sum, min);
}