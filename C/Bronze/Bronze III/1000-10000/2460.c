#include <stdio.h>

int main() {
    int up, down, max = 0;
    int temp = 0;
    
    for (int i=0; i<10; i++) {
        scanf("%d %d", &down, &up);
        temp += up - down;
        if (max < temp) max = temp;
    }
    printf("%d", max);

    return 0;
}