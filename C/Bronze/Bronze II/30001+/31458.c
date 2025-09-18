#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int T;
    char str[62];
    scanf("%d", &T);

    for (int i=0; i<T; i++) {
        int num, idx;
        scanf("%s", str);

        int length = strlen(str);

        for (int j=0; j<length; j++) {
            if (str[j] >= 48 && str[j] <= 57) {
                num = str[j] - 48;
                idx = j;
                break;
            }
        }
        if (length == 1) {
            printf("%d\n", num);
        }
        else if (idx == 0) {
            printf("%d\n", 1);
        }
        else if (length-1 == idx) {
            if (idx%2) printf("%d\n", abs(num - 1));
            else printf("%d\n", num);
        }
        else {
            if (idx%2) printf("%d\n", 0);
            else printf("%d\n", 1);
        }
    }
}