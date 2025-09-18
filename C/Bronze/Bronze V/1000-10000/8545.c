#include <stdio.h>

int main() {
    char str[3];
    scanf("%s", str);

    for (int i=2; i>=0; i--) {
        printf("%c", str[i]);
    }
}