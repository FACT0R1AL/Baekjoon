#include <stdio.h>

int main() {
    int n, cnt = 0;
    int temp, tempNum, temp2;
    scanf("%d", &n);

    temp2 = n;
    temp = n/10 + n%10;
    tempNum = n%10;
    
    do {
        temp = temp2/10 + temp2%10;
        tempNum = temp2%10;
        temp2 = tempNum*10 + temp%10;
        cnt++;
    } while (n != temp2);

    printf("%d", cnt);
}