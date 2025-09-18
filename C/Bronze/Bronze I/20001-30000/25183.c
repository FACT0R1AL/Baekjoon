#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, cnt = 1;
    char str[100001];
    scanf("%d", &n);
    scanf("%s", str);

    for (int i=0; i<n-1; i++) {
        if (abs(str[i] - str[i+1]) == 1) {
            cnt++;
        }
        else {
            cnt = 1;
        }

        if (cnt == 5) {
            printf("YES");
            return 0;
        }
    }

    printf("NO");
}