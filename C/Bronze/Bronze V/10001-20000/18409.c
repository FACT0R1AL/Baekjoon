#include <stdio.h>

int main() {
    char str[51];
    int n, cnt = 0;
    scanf("%d", &n);
    scanf("%s", str);

    for (int i=0; i<n; i++) {
        if (str[i] == 'a') cnt++;
        else if (str[i] == 'e') cnt++;
        else if (str[i] == 'i') cnt++;
        else if (str[i] == 'o') cnt++;
        else if (str[i] == 'u') cnt++;
    }

    printf("%d", cnt);
}