#include <stdio.h>

int main() {
    int board[100][100] = {0,};
    int n, m, cnt = 0;
    int x1, y1, x2, y2;
    scanf("%d %d", &n, &m);

    for (int i=0; i<n; i++) {
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);

        if (x2 < x1) {
            int temp = x1;
            x1 = x2;
            x2 = temp;
        }
        if (y2 < y1) {
            int temp = y1;
            y1= y2;
            y2 = temp;
        }

        for (int j=y1-1; j<=y2-1; j++) {
            for (int k = x1-1; k <= x2-1; k++) {
                board[j][k]++;
            }
        }
    }

    for (int i=0; i<100; i++) {
        for (int j=0; j<100; j++) {
            if (board[i][j] > m) cnt++;
        }
    }

    printf("%d", cnt);
}