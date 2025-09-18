#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        int x1, y1, r1, x2, y2, r2;
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        double distance = sqrt(abs(x1-x2)*abs(x1-x2) + abs(y1-y2)*abs(y1-y2));

        if (x1 == x2 && y1 == y2 && r1 == r2) printf("-1\n");
        else if (abs(r1-r2) < distance && distance < abs(r1+r2)) printf("2\n");
        else if (distance == abs(r1-r2) || distance == abs(r1+r2)) printf("1\n");
        else printf("0\n");
    }

    return 0;
}