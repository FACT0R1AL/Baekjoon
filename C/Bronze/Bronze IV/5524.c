#include <stdio.h>
#include <string.h>

int main() {
    int n;
    char str[101][101];
    scanf("%d", &n);
    
    for (int i=0; i<n; i++) {
        scanf("%s", &str[i]);
    }
    
    for (int i=0; i<n; i++) {
        int length = strlen(str[i]);
        
        for (int j=0; j<length; j++) {
            if (str[i][j] >= 65 && str[i][j] <= 90) str[i][j] += 32;
        }
    }
    
    for (int i=0; i<n; i++) {
        printf("%s\n", str[i]);
    }
}