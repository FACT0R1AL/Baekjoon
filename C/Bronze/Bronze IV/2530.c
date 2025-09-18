#include <stdio.h>

int main() {
    int h, m, s;
    int plusSecond;
    scanf("%d %d %d", &h, &m, &s);
    scanf("%d", &plusSecond);

    int temp = h * 3600 + m * 60 + s + plusSecond;
    h = (temp / 3600) % 24;
    temp %= 3600;
    m = temp / 60;
    temp %= 60;
    s = temp;
    
    printf("%d %d %d", h, m, s);
    return 0;
}