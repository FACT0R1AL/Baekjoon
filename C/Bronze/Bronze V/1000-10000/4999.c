#include <stdio.h>
#include <string.h>

int main() {
    char person[1001], doctor[1001];
    scanf("%s", person);
    scanf("%s", doctor);

    int lengthP = strlen(person);
    int lengthD = strlen(doctor);

    if (lengthP >= lengthD) printf("go");
    else printf("no");
}