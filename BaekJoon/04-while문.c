// 10952_A+B-5
/*#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int A, B;

	while (1) {
		scanf("%d %d", &A, &B);

		if ((A == 0) && (B == 0)) {
			break;
		}

		printf("%d\n", A + B);
	}

	return 0;
}

// 10951_A+B-4
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int A, B;

	while (scanf("%d %d", &A, &B) != EOF) {
		printf("%d\n", A + B);
	}

	return 0;
}

// 1110_더하기 사이클
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, a, b, c;
	int new_num = 0, cycle = 0;

	scanf("%d", &N);		// 초기 숫자 입력
	new_num = N;		// 입력한 수 new_num에 대입

	while (1) {		// new_num과 N과 같지 않을 때 동안
		a = new_num / 10;		// 10의 자리 숫자
		b = new_num % 10;		// 1의 자리 숫자

		c = a + b;		//		10의 자리 수와 1의 자리 수 더한 수

		if (c >= 10) {		// c가 2자리 숫자라면
			c = c % 10;		// 1의 자리 숫자를 구해 c에 대입
		}

		new_num = (b * 10) + c;		// 새로운 수
		//printf("%d %d %d %d", a, b, c, new_num);

		cycle++;		// 횟수 더하기

		if (new_num == N) {		// 새로운 수와 처음 입력한 값이 같다면
			printf("%d", cycle);		// 사이클의 길이 구하기
			break;
		}
	}

	return 0;
}*/