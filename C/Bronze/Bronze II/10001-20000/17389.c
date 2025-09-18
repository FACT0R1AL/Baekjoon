#include <stdio.h>

int main() {
    int n, score = 0, bonus = 0;
    char quiz[10001];
    scanf("%d", &n);
    scanf("%s", quiz);

    for (int i=0; i<n; i++) {
        if (quiz[i] == 'O') {
            score += i+1 + bonus;
            bonus++;
        }
        else {
            bonus = 0;
        }
    }

    printf("%d", score);
}