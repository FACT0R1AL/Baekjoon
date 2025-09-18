#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[3], sum = 0, idx;
    double avg;
    int min = 101;

    for (int i=0; i<3; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    avg = sum/3.0;

    for (int i=0; i<3; i++) {
        if (min > abs(arr[i]-avg)){
            min = abs(arr[i]-avg);
            idx = i;
        }
    }

    printf("%d", arr[idx]);
}