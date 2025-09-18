#include <stdio.h>

void reset(int board[51]) {
    for (int i=0; i<51; i++) {
        board[i] = 0;
    }
}

int main() {
    int n, max = 0, answer = 0;
    int arr[51], ship[51];
    int idx = 0, equalmax[51] = {0,};
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%d %d", &arr[i], &ship[i]);
    }

    for (int i=0; i<n; i++) {
        int sum = 0;
        int money = arr[i];

        for (int j=0; j<n; j++) {
            if (arr[j] >= money && money - ship[j] > 0) sum += money - ship[j];
        }

        if (sum > max) {
            max = sum;
            answer = money;

            reset(equalmax);
            idx = 0;
            equalmax[idx] = money;
            idx++;
        }

        else if (sum == max) {
            equalmax[idx] = money;
            idx++;
        }
    }

    if (max == 0) printf("0");
    else {
        int min = 2147483647;

        for (int i=0; i<51; i++) {
            if (equalmax[i] == 0) break;
            if (min > equalmax[i]) min = equalmax[i];
        }

        printf("%d", min);
    }
}