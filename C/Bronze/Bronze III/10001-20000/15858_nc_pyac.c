#include <stdio.h>

int main() {
    double a,b,c;
    double answer;
    scanf("%lf %lf %lf", &a, &b, &c);

    answer = a*b/c;
    printf("%lf\n", answer);

    return 0;
}