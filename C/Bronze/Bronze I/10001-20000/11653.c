#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, div = 0;
    scanf("%d", &n);
    char* prime = (char*)malloc(n+1);

    for (int i=1; i<n; i++) {
        prime[i] = 1;
    }

    prime[1] = 0;
    prime[2] = 1;

	for (int i = 2; i * i <= n; i++) {
		if (prime[i]) {
			for (int j = i * i; j <= n; j += i) {
				prime[j] = 0;
            }
		}
	}

    while (n != 1) {
        div = 0;
        for (int i=2; i<=n; i++) {
            if (n % i == 0 && prime[i]) {
                n /= i;
                div = 1;
                printf("%d\n", i);
                break;
            }
        }
        if (!div) {
            printf("%d\n", n);
            break;
        }
    }

    free(prime);
    return 0;
}