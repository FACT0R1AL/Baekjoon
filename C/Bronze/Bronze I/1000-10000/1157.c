#include <stdio.h>
#include <string.h>

int main() {
    char s[1000000];
    int arr[26];
    int max[2] = {-1, 96};
    scanf("%s", s);

    int length = strlen(s);

    for (int i=0; i<length; i++) {
        if (s[i] >= 65 && s[i] <= 90) {
            arr[s[i]-65] += 1;
        }
        else if (s[i] >= 97 && s[i] <= 122) {
            arr[s[i]-97] += 1;
        }
    }

    for (int i=0; i<26; i++) {
        if (max[0] < arr[i]) {
            max[0] = arr[i];
            max[1] = i+65;
        }
        else if (max[0] == arr[i] && max[0] != 0) {
            max[1] = 63;
        }
    }

    printf("%c", max[1]);
}