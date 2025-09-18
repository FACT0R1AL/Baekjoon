#include <stdio.h>
#include <string.h>

int main() {
    char a[8], b[8];
    int lengthA, lengthB, min;

    scanf("%s %s", a, b);

    lengthA = strlen(a);
    lengthB = strlen(b);

    min = lengthA <= lengthB ? lengthA : lengthB;

    if (lengthA > lengthB) {
        for (int i=0; i<lengthA-lengthB; i++) {
            printf("%d", a[i]-'0');
        }
        for (int i=0; i<min; i++) {
            printf("%d", (a[i+lengthA-lengthB]-'0') + (b[i]-'0'));
        }
    }
    else if (lengthA < lengthB) {
        for (int i=0; i<lengthB-lengthA; i++) {
            printf("%d", b[i]-'0');
        }
        for (int i=0; i<min; i++) {
            printf("%d", (a[i]-'0') + (b[i+lengthB-lengthA]-'0'));
        }
    
    }
    else {
        for (int i=0; i<min; i++) {
            printf("%d", (a[i]-'0') + (b[i]-'0'));
        }
    }
}