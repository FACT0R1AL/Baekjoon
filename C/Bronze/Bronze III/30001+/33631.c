#include <stdio.h>
#include <stdbool.h>

int main() {
    int have[4], need[4], Q = 0, cnt = 0;

    for (int i=0; i<4; i++) {   //가지고 있는 것들 받기
        scanf("%d", &have[i]);  //밀가루 / 초콜릿 / 달걀 / 버터
    }

    for (int i=0; i<4; i++) {   //쿠키 한개 만드는데 필요한 것들 받기
        scanf("%d", &need[i]);
    }

    scanf("%d", &Q);

    for (int i=0; i<Q; i++) {
        int way, ii;
        scanf("%d %d", &way, &ii);

        if (way >= 2) {
            have[way-2] += ii;
            printf("%d\n", have[way-2]);
        }
        else {
            bool flag = true;
            for (int j=0; j<4; j++) {
                if (need[j]*ii > have[j]) flag = false;
            }

            if (flag) {
                for (int j=0; j<4; j++) {
                    have[j] -= need[j] * ii;
                }
                cnt += ii;
                printf("%d\n", cnt);
            }
            else printf("Hello, siumii\n");
        }
    }

    return 0;
}