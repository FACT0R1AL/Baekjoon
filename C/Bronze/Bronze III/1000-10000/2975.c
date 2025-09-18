#include <stdio.h>

int main() {
    int money, pay;
    char type;

    while (1) {
        scanf("%d", &money);
        scanf(" %c", &type);
        scanf("%d", &pay);

        if (money == 0 && type == 'W' && pay == 0) break;

        if (type == 'D') printf("%d\n", money+pay);
        else {
            if (pay > 200) printf("Not allowed\n");
            else if (money-pay < -200) printf("Not allowed\n");
            else printf("%d\n", money-pay);
        }
    }
}