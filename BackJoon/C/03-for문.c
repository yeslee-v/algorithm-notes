// 2739_구구단
/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N;
	int i;

	scanf("%d", &N);

	for (i = 1; i < 10; i++) {
		printf("%d * %d = %d\n", N, i, N * i);
	}

	return 0;
}

// 10950_A+B-3
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int T;
	int A, B;
	int i;

	scanf("%d\n", &T);

	for (i = 0; i < T; i++) {
		scanf("%d %d", &A, &B);

		printf("%d\n", A + B);
	}

	return 0;
}

// 8393_합
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	int n;
	int i, j = 0;

	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		j += i;
	}

	printf("%d", j);

	return 0;
}

// 15552_빠른 A+B
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	int T;
	int A, B;
	int i;

	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		scanf("%d%d", &A, &B);
		printf("%d\n", A + B);
	}

	return 0;
}

// 2741_N 찍기
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, i;

	scanf("%d", &N);
	for (i = 1; i <= N; i++) {
		printf("%d\n", i);
	}

	return 0;
}

// 2742_기찍 N
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, i;

	scanf("%d", &N);

	for (i = N; i > 0; i--) {
		printf("%d\n", i);
	}

	return 0;
}

// 11021_A+B-7
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int T, A, B, i;

	scanf("%d", &T);

	for (i = 1; i <= T; i++) {
		scanf("%d%d", &A, &B);
		printf("Case #%d: %d\n", i, A + B);
	}

	return 0;
}

// 11022_A+B-8
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int T, A, B, i;

	scanf("%d", &T);

	for (i = 1; i <= T; i++) {
		scanf("%d%d", &A, &B);
		printf("Case #%d: %d + %d = %d\n", i, A, B, A + B);
	}

	return 0;
}

// 2438_별 찍기
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, i, j;

	scanf("%d", &N);

	for (i = 1; i <= N; i++) {
		for (j = 1; j <= N; j++) {
			if (i + j > N) {
				printf("*");
			}
			else {
				printf(" ");
			}
			//printf("i: %d j: %d\n", i, j);
		}
		printf("\n");
	}

	return 0;
}

// 10871_X보다 작은 수
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, X, a, i;

	scanf("%d %d", &N, &X);
	for (i = 0; i < N; i++) {
		scanf("%d", &a);

		if (a < X) {
			printf("%d ", a);
		}
	}

	return 0;
}*/