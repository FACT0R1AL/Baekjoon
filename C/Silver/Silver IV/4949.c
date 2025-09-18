#include <stdio.h>
#include <string.h>

char stack[105];
int top = -1;

void push(char ch) {
    stack[++top] = ch;
}
int pop(char ch) {
    if (top == -1) return 0;
    else if (stack[top] == '[' && ch != ']') return 0;
    else if (stack[top] == '(' && ch != ')') return 0;
    else {
        top--;
        return 1;
    }
}

int main() {
    char temp, s[105];

    while (1) {
        top = -1;
        fgets(s, sizeof(s), stdin);
        s[strcspn(s, "\n")] = 0;
        if (s[0] == '.') break;

        int length = strlen(s);
        int flag = 0;

        for (int i=0; i<length; i++) {
            if (s[i] == '(') {
                push('(');
            }
            else if (s[i] == '[') {
                push('[');
            }
            else if (s[i] == ')') {
                if (pop(')') == 0) {
                    printf("no\n");
                    flag = 1;
                    break;
                }
            }
            else if (s[i] == ']') {
                if (pop(']') == 0) {
                    printf("no\n");
                    flag = 1;
                    break;
                }
            }
        }

        if (flag == 0) {
            if (top == -1) printf("yes\n");
            else printf("no\n");
        }
    }
    return 0;
}