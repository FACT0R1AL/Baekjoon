#include <stdio.h>
#include <string.h>

int prime(int n) {
    if (n == 1 || n==2) return 1;

    for (int i=2; i<n; i++) {
        if (n % i == 0) return 0;
    }

    return 1;
}
int main() {
    char str[21];   //A = 65 - 90, a = 97 - 122
    int sum = 0;
    scanf("%s", str);

    int length = strlen(str);

    for (int i=0; i<length; i++) {
        if (str[i] >= 65 && str[i] <= 90) sum += str[i] - 38;
        else sum += str[i] - 96;
    }
    
    if (prime(sum)) printf("It is a prime word.");
    else printf("It is not a prime word.");
}