#include <stdio.h>

int main() {
    int n;        //0 = decrease, 1 = increase
    int arr[3], mode[2];
    scanf("%d", &n);

    printf ("Gnomes:\n");

    for (int i=0; i<n; i++) {
        int flag = 0;

        for (int j=0; j<3; j++) {
            scanf("%d", &arr[j]);
        }

        for (int j=1; j<3; j++) {
            if (arr[j-1] > arr[j]) {
                mode[j-1] = 0;
            }
            else if (arr[j-1] < arr[j]) {
                mode[j-1] = 1;
            }
            else {
                flag = 1;
            }
        }
        if (mode[0] != mode[1]) {
            printf("Unordered\n");
        }
        else if (flag || mode[0] == mode[1]) {
            printf("Ordered\n");
        }
    }
}