#include <stdio.h>

int main() {
    int h, m, t;
    scanf("%d %d", &h, &m);
    scanf("%d", &t);

    int hm = h*60 + m + t;
    h = hm / 60;
    m = hm % 60;

    if (h >= 24) h -= 24;
    printf("%d %d", h, m);
}