#include <stdio.h>
#include <string.h>

char stack[100001];
int top = -1;

void push(int a) {
    stack[++top] = a;
}

void pop() {
    top--;
}
int main() {
    int n, sum = 0;
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        int m;
        scanf("%d", &m);
        if (m != 0) push(m);
        else pop();
    }

    for (int i=0; i<top+1; i++) {
        sum += stack[i];
    }

    printf("%d", sum);
}