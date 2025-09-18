#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, m;
    int x1, x2, y1, y2;
    scanf("%d %d", &n, &m);
    scanf("%d %d", &x1, &y1);
    scanf("%d %d", &x2, &y2);

    if ((abs(x1-x2)%2 == 0 && y1 == y2 && (x1+x2)/2 <= m && (y1+y2)/2 <= n) || //(3,1) (1,1) (3,1) 
        (abs(y1-y2)%2 == 0 && x1 == x2 && (x1+x2)/2 <= m && (y1+y2)/2 <= n) ||
         abs(x1-x2) == abs(y1-y2) || 
        (abs(x1-x2)+abs(y1-y2))%2 == 0 && x1+x2 <= n && y1+y2 <= m) printf("YES\n");
    else printf("NO\n");

    // for (int i=1; i<=n; i++) {
    //     for (int j=1; j<=m; j++) {
    //         printf("(%d,%d) ", i, j);
    //     }

    //     printf("\n");
    // }
}