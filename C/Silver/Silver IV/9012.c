#include <stdio.h>
#include <string.h>

char stack[51];
int top = -1;

void push(char ch) {
    stack[++top] = ch;
}

int pop() {
    if (top == -1) return 0;
    else {
        top--;
        return 1;
    }
}

int main() {
    int n;
    char s[51];
    scanf("%d", &n);

    for (int i=0; i<n; i++) {
        scanf("%s", s);
        int length = strlen(s);
        int flag = 0;

        for (int j=0; j<length; j++) {
            if (s[j] == '(') {
                push('(');
            }
            else if (s[j] == ')') {
                if (pop() == 0) {
                    printf("NO\n");
                    flag = 1;
                    break;
                }
            }
        }

        if (flag == 0) {
            if (top == -1) printf("YES\n");
            else printf("NO\n");
        }
        
        top = -1;
    }


}