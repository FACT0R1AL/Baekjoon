#include <stdio.h>

int main() {
    int h, w;
    int dh, dw, ph, pw;
    int cnt = 0, cntrow = 0;;

    char board[100][100];

    scanf("%d %d", &h, &w);
    scanf("%d %d %d %d", &dh, &dw, &ph, &pw);

    for (int i=0; i<h; i++) {
        scanf("%s", board[i]);
    }

    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            if (board[i][j] == 'P') cntrow++;
        }

        if (cntrow == pw) cnt++;
        cntrow = 0;
    }
    
    if (cnt != ph) printf("1");
    else printf("0");
}