#include <stdio.h>

int main() {
    int h, w;
    char board[50][50];
    scanf("%d %d", &h, &w);

    int cnt = 0, max = 0;
    
    for (int i=0; i<h; i++) {
        scanf("%s", board[i]);
    }

    char prevWB = board[0][0], WB = board[0][1], firstWB = board[0][0];

    for (int a=0; a<=h-8; a++) {
        for (int b=0; b<=w-8; b++) {
            for (int i=a; i<8+a; i++) {
                for (int j=b; j<8+b; j++) {
                    firstWB = board[i][0];
                    prevWB = WB;
                    WB = board[i][j];
                    if (j==0 && firstWB == prevWB) {
                        cnt++;
                        printf("first %d %d\n", i, j);
                    }
                    else if (prevWB != WB) {
                        cnt++;
                        printf("!= %d %d\n", i, j);
                    }
                }
            }
            if (max < cnt) max = cnt;
            printf("%d/%d, cnt : %d\n", a, b, cnt);
            cnt = 0;
        }
    }
}