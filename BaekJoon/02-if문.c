// 1330_두 수 비교하기
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int A, B;

	scanf("%d %d", &A, &B);

	if (A > B) {
		printf(">");
	}

	else if (A < B) {
		printf("<");
	}
	else
		printf("==");

	return 0;
}

// 9498_시험 성적
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	int score;

	scanf("%d", &score);

	if (score >= 90)	printf("A");
	else if (score >= 80)	printf("B");
	else if (score >= 70)	printf("C");
	else if (score >= 60)	printf("D");
	else {
		printf("F");
	}

	return 0;
}

// 2753_윤년
#include <stdio.h>
int main(void) {
	int year;

	scanf_s("%d", &year);
	if ((year % 4) == 0) && ((year % 100) != 0) || ((year % 400) == 0))
	printf("%d", 1);
	else
		printf("%d", 0);

	return 0;
}

// 14681_사분면 고르기
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int x;
	int y;

	scanf("%d%d", &x, &y);

	if ((x > 0) && (y > 0)) {
		printf("%d", 1);
	}
	else if ((x < 0) && (y > 0)) {
		printf("%d", 2);
	}
	else if ((x < 0) && (y < 0)) {
		printf("%d", 3);
	}
	else if ((x > 0) && (y < 0)) {
		printf("%d", 4);
	}

	return 0;
}

// 2884_알람시계
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int H, M;

	scanf("%d%d", &H, &M);

	if (M > 45) {
		printf("%d %d", H, (M - 45));
	}

	else if (M < 45) {
		if (H == 0) {
			printf("%d %d", 23, 60 + (M - 45));
		}
		else if (H > 0) {
			printf("%d %d", (H - 1), 60 + (M - 45));
		}
	}

	else {
		printf("%d", H);
	}

	return 0;
}