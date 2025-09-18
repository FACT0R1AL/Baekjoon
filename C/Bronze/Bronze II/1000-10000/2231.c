#include <stdio.h>
#include <string.h>
#include <math.h>

int digits(int n) {
    if(n == 0) return 0;
    while(n != 0) return 1 + digits(n/10);
    return 0;
}

int main() {
    int flag = 0, dep = 0;
    char num[7];
    scanf("%d", &dep);

    for (int i=1; i<dep; i++) { //i = generator
        if (flag) break;

        int generator = i;
        int sum = 0;
        int length = digits(i);
        
        for (int j=1; j<=length; j++) {
            int temp = pow(10, j);
            if (length == j) sum += generator / (temp / 10);
            else sum += (generator % temp) / (temp / 10);
        }

        if (dep == generator + sum) {
            printf("%d", generator);
            flag = 1;
        }
    }

    if (!flag) printf("0");

}