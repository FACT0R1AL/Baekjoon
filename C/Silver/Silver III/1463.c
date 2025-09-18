#include <stdio.h>

int min (int a, int b) {
    if (a > b) return b;
    else return a;
}
int main() {
    int n, cnt = 0;
    int dp[1000001];
    dp[1] = 0;
    scanf("%d", &n);

    for(int i=2; i<=n; i++) {
        int Nmin = dp[i-1];
        if(i % 2 == 0)
            Nmin = min(Nmin, dp[i/2]);
        if(i % 3 == 0)
            Nmin = min(Nmin, dp[i/3]);
        dp[i] = Nmin + 1;
    }
    
    printf("%d", dp[n]);
    return 0;
}