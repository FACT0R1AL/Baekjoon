#include <stdio.h>
#include <stdbool.h>

int main() {
    int n;
    char str[101];
    bool isChecked[101] = {false, };
    scanf("%d", &n);
    scanf("%s", str);

    for (int i=0; i<n; i++) {
        if (str[i] == 'P' && isChecked[i] == false) {
            for (int j=i; j<n; j++) {
                if (str[j] == 'C' && isChecked[j] == false) {
                    char temp = str[i];
                    str[i] = str[j];
                    str[j] = temp;
                    isChecked[i] = true;
                    isChecked[j] = true;
                    break;
                }
            }
        }
        else if (str[i] == 'C' && isChecked[i] == false) {
            for (int j=i; j<n; j++) {
                if (str[j] == 'P' && isChecked[j] == false) {
                    char temp = str[i];
                    str[i] = str[j];
                    str[j] = temp;
                    isChecked[i] = true;
                    isChecked[j] = true;
                    break;
                }
            }
        }
    }

    printf("%s", str);
    return 0;
}