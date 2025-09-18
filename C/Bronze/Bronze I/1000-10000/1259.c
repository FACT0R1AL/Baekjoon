#include <stdio.h>
#include <string.h>

int main() {
    char nums[6];

    while (1) {
        int check = 1;
        scanf("%s", nums);
        int length = strlen(nums);

        if (nums[0] - '0' == 0) break;

        for (int i=0; i<length/2; i++) {
            if (nums[i] != nums[length-i-1]) check = 0;
        }

        if (check) printf("yes\n");
        else printf("no\n");
    }
    return 0;
}