#include <stdio.h>

void printArr(int arr[5]) {
    for (int i=0; i<5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[5];
    
    for (int i=0; i<5; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i=0; i<5; i++) {
        for (int j=1; j<5; j++) {
            if (arr[j-1] > arr[j]) {
                int temp = arr[j-1];
                arr[j-1] = arr[j];
                arr[j] = temp;
                
                printArr(arr);
            }
        }
    }
}