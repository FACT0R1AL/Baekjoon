#include <stdio.h>
#include <string.h>

int main() {
    char a[10001], b[10001];
    int la, lb;
    long long int sum = 0;

    scanf("%s %s", a, b);

    la = strlen(a);
    lb = strlen(b);

    for (int i=0; i<la; i++) {
        for (int j=0; j<lb; j++) {
            sum += (a[i] - '0') * (b[j] - '0');
        }
    }

    printf("%lld", sum);
}