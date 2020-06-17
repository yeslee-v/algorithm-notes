// 2557_Hello World
/*#include <stdio.h>
int main(void) {
	printf("Hello World!");

	return 0;
}

// 110718_WeloveKriii
#include<stdio.h>
int main(void) {
	//char ch[20] = "강한친구 대한육군";

	printf("%s\n%s", "강한친구 대한육군", "강한친구 대한육군");

	return 0;
}

// 10171_고양이
#include<stdio.h>
int main(void) {
	printf("\\    /\\\n");
	printf(" )  ( ')\n");
	printf("(  /  )\n");
	printf(" \\(__)|\n");

	return 0;
}

// 10172_개
#include<stdio.h>
int main(void) {
	printf("|\\_/|\n");
	printf("|q p|   /}\n");
	printf("( 0 )\"\"\"\\\n");
	printf("|\"^\"`    |\n");
	printf("||_/=\\\\__|\n");

	return 0;
}

// 1000,1001,10998_A+B A-B A*B 
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	int A, B;

	scanf("%d%d", &A, &B);
	printf("%d\n", A * B);

	return 0;

}

// 1008_A/B
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void) {
	int A, B;

	scanf("%d%d", &A, &B);
	printf("%.15g\n", (double)A / B);

	return 0;

}

// 10869_사칙연산
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int A, B;

	scanf("%d%d", &A, &B);
	printf("%d\n", A + B);
	printf("%d\n", A - B);
	printf("%d\n", A * B);
	printf("%d\n", A / B);
	printf("%d\n", A % B);

	return 0;
}

// 10430_나머지
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int A, B, C;

	scanf("%d%d%d", &A, &B, &C);

	printf("%d\n", (A + B) % C);
	printf("%d\n", ((A % C) + (B % C)) % C);
	printf("%d\n", (A * B) % C);
	printf("%d\n", (A % C) * (B % C) % C);

	return 0;
}

// 2588_곱셈
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void) {
	int a, b;
	int c, d, e;
	int i, j;

	scanf("%d%d", &a, &b);

	i = b % 10;
	c = a * i;

	j = b / 10;
	i = j % 10;
	d = a * i;

	j = j / 10;
	e = a * j;

	//printf("%d %d %d %d %d", a, b, c, d, e);

	printf("%d\n%d\n%d\n%d", c, d, e, c + (d * 10) + (e * 100));

	return 0;
}*/