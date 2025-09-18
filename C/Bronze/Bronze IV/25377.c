#include <stdio.h>

int main() {
    int T;
    int min = 2147483647;
    int pri = 2147483647;

    scanf("%d", &T);

    for (int i=0; i<T; i++) {
        int a, b;
        scanf("%d %d", &a, &b);

        if (b >= a && min > b) {
            min = b;
        }
    }
    
    if (min == 2147483647) printf("-1");
    else printf("%d", min);
}