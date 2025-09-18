#include <stdio.h>

char arr[10001];

int d(int n) {
    int sum = 0;
    int temp = n;

    for (int i=1; i<=4; i++) {
        sum += n%10;
        n /= 10;
    }
    
    return temp + sum;
}

int main() {
    for (int i=1; i<=10000; i++) {
        int temp = i;
        if (arr[temp] == 0) {
            printf("%d\n", temp);

            while (temp < 10000) {
                temp = d(temp);
                arr[temp] = 1;
            }
        }
    }
}