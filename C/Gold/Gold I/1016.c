#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

int main() {
    long long int a, b;
    int idx = 0, cnt = 0;

    scanf("%lld %lld", &a, &b);
    int size = b-a+1;
    bool* arr = (bool*)malloc(sizeof(bool) * size); //1 - 1000001

    for (int i=0; i<size; i++) {
        arr[i] = true;
    }

    long long sqrtb = sqrt(b);

    for (long long int i=2; i<=sqrtb; i++) {
        long long int sqr = i*i;
        long long int start = ((a + sqr - 1) / sqr) * sqr;

        for (long long int j = start; j <= b; j += sqr) {
            arr[j-a] = false;
        }
    }

    for (int i=0; i<size; i++) {
        if (arr[i]) cnt += 1;
    }

    printf("%d", cnt);
    free(arr);

    return 0;
}