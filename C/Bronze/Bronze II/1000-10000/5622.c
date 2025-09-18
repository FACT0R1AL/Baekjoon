#include <stdio.h>
#include <string.h>

int main() {
    char str[16];
    int cnt = 0;
    scanf("%s", str);
    int n = strlen(str);

    for (int i=0; i<n; i++) {
        if (str[i] >= 'A' && str[i] <= 'C') {
            cnt += 3;
        }
        else if (str[i] <= 'F') {
            cnt += 4;
        }
        else if (str[i] <= 'I') {
            cnt += 5;
        }
        else if (str[i] <= 'L') {
            cnt += 6;
        }
        else if (str[i] <= 'O') {
            cnt += 7;
        }
        else if (str[i] <= 'S') {
            cnt += 8;
        }
        else if (str[i] <= 'V') {
            cnt += 9;
        }
        else if (str[i] <= 'Z') {
            cnt += 10;
        }
    }
    printf("%d", cnt);
}