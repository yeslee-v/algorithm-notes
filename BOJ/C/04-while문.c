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

// 1110_���ϱ� ����Ŭ
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int N, a, b, c;
	int new_num = 0, cycle = 0;

	scanf("%d", &N);		// �ʱ� ���� �Է�
	new_num = N;		// �Է��� �� new_num�� ����

	while (1) {		// new_num�� N�� ���� ���� �� ����
		a = new_num / 10;		// 10�� �ڸ� ����
		b = new_num % 10;		// 1�� �ڸ� ����

		c = a + b;		//		10�� �ڸ� ���� 1�� �ڸ� �� ���� ��

		if (c >= 10) {		// c�� 2�ڸ� ���ڶ��
			c = c % 10;		// 1�� �ڸ� ���ڸ� ���� c�� ����
		}

		new_num = (b * 10) + c;		// ���ο� ��
		//printf("%d %d %d %d", a, b, c, new_num);

		cycle++;		// Ƚ�� ���ϱ�

		if (new_num == N) {		// ���ο� ���� ó�� �Է��� ���� ���ٸ�
			printf("%d", cycle);		// ����Ŭ�� ���� ���ϱ�
			break;
		}
	}

	return 0;
}*/