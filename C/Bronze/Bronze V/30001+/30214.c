#include <stdio.h>

int main() {
    int a, b;
    double percent;
    scanf("%d %d", &a, &b);

    percent = a/(float)b;

    if (percent >= 0.5) printf("E");
    else printf("H");
}