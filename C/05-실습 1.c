// 10039_평균 점수
/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int ws, sh, sk, s, ks;
	int i, sum = 0, avg = 0;

	scanf("%d", &ws);
	scanf("%d", &sh);
	scanf("%d", &sk);
	scanf("%d", &s);
	scanf("%d", &ks);

	int stu[5] = { ws, sh, sk, s, ks };

	for (i = 0; i < 5; i++) {
		if (stu[i] < 40) {
			stu[i] = 40;
			sum += stu[i];
		}
		else {
			sum += stu[i];
		}

	}

	avg = sum / 5;

	printf("%d", avg);

	return 0;
}

// 5543_상근날드
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int burger_h, burger_m, burger_l;
	int coke, cider;
	int burger_cheap, drink_cheap;
	int set_cheap;

	scanf("%d", &burger_h);
	scanf("%d", &burger_m);
	scanf("%d", &burger_l);
	scanf("%d", &coke);
	scanf("%d", &cider);

	if (burger_h > burger_m) {
		if (burger_m > burger_l) {
			burger_cheap = burger_l;
		}
		else {
			burger_cheap = burger_m;
		}
	}
	else {
		if (burger_h > burger_l) {
			burger_cheap = burger_l;
		}
		else {
			burger_cheap = burger_h;
		}
	}

	if (coke > cider) {
		drink_cheap = cider;
	}
	else {
		drink_cheap = coke;
	}

	set_cheap = (burger_cheap + drink_cheap) - 50;

	printf("%d", set_cheap);

	return 0;
}

// 10817_세 수
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int a, b, c, mid;

	scanf("%d %d %d", &a, &b, &c);

	if ((a > b) && (a> c)) {
		if (b > c) {
			mid = b;
		}
		else {
			mid = c;
		}
	}
	else if((b>a) && (b>c)) {
		if (a > c) {
			mid = a;
		}
		else {
			mid = c;
		}
	}

	else {
		if (a > b) {
			mid = a;
		}
		else {
			mid = b;
		}
	}

	printf("%d", mid);

	return 0;
}

// 2523_별 찍기-13
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, i, j;
	int m, n;

	scanf("%d", &N);

	for (i = 0; i < N; i++) {
		for (j = 0; j <= i; j++) {
			printf("*");
		}
		printf("\n");
		
		if (i == (N-1)) {
			for (m = N - 1; m > 0; m--) {
				for (n = m; n > 0; n--) {
					printf("*");
				}
				printf("\n");
			}
		}
	}

	return 0;
}

// 2446_별 찍기-9
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, i, j, k;

	scanf("%d", &N);

	for (i = 1; i <= N; i++) {		// 위
		for (j = i - 1; j > 0; j--) {		// 왼쪽 공백
			printf(" ");
		}
		for (k = (2 * N - 2 * i + 1); k > 0; k--) {		// 오른쪽 별
			printf("*");
		}
		printf("\n");
	}

	for (i = N - 1; i > 0; i--) {		// 아래
		for (j = i - 1; j > 0; j--) {		// 왼쪽 공백
			printf(" ");
		}
		for (k = (2 * N - 2 * i + 1); k > 0; k--) {		// 오른쪽 별
			printf("*");
		}
		printf("\n");
	}

	return 0;
}

// 10996_별 찍기 - 21
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, i, j;

	scanf("%d", &N);
	for (i = 0; i < (2 * N); i++) {
		for (j = 0; j < N; j++) {
			if ((i % 2) == (j % 2)) {
				printf("*");
			}
			else {
				printf(" ");
			}
		}
		if (N == 1) {
			if ((i == 0) && (j == 0)) {
				printf("\n");
			}
		}
		else if ((i != (2 * N - 1)) && (j != (N - 1))) {
			printf("\n");
		}
	}

	return 0;
}*/