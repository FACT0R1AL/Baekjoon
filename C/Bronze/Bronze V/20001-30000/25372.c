#include <stdio.h>
#include <string.h>

int main() {
    char str[101];
    int n, length;
    scanf("%d", &n);
    
    for (int i=0; i<n; i++) {
        scanf("%s", str);
        length = strlen(str);
        if (length >= 6 && length <= 9) printf("yes\n");
        else printf("no\n");
    }
}