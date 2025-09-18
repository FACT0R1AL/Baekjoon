#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n, x, length = 0;
    int arr[10000] = {0};
    char cmd[6];
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%s", cmd);

        if (cmd[0] == 'p' && cmd[1] == 'u') {
            length++;
            scanf("%d", &x);
            arr[length-1] = x;
        }
        else if (cmd[0] == 'p' && cmd[1] == 'o') {
            if (length == 0) printf("-1\n");
            else {
                printf("%d\n", arr[length-1]);
                arr[length-1] = 0;
                length--;
            }
        }
        else if (cmd[0] == 't') {
            if (length == 0) printf("-1\n");
            else printf("%d\n", arr[length-1]);
        }
        else if (cmd[0] == 's') {
            printf("%d\n", length);
        }
        else if (cmd[0] == 'e') {
            if (length == 0) printf("1\n");
            else printf("0\n");
        }
    }
}