#include <stdio.h>
#include <string.h>

int main() {
    char str[30005], key[100001];
    fgets(str, 30002, stdin);
    scanf("%s", key);

    int strLen = strlen(str) - 1;
    int keyLen = strlen(key);

    for (int i=0; i<strLen; i++) {
        if (str[i] == ' ') printf(" ");
        else if (str[i] - (key[i%keyLen] - 96) < 97) printf("%c", str[i] - (key[i%keyLen] - 96) + 26);
        else printf("%c", str[i] - (key[i%keyLen] - 96));
    }
}