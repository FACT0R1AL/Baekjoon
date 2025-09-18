#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    while (1) {
        int alphabet[26] = {0,};
        char str[255];
        int cnt = 0;

        fgets(str, 252, stdin);
        int length = strlen(str) - 1;

        if (str[0] == '#' && length == 1) break;

        for (int i=0; i<length; i++) {
            if (str[i] >= 'A' && str[i] <= 'Z') str[i] += 32;
            if (str[i] >= 'a' && str[i] <= 'z' && 
                alphabet[str[i] - 'a'] == 0) 
                {alphabet[str[i] - 'a'] = 1; cnt++;}
        }

        printf("%d\n", cnt);
    }
}