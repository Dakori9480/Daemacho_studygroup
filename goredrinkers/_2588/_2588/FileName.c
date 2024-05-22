#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main() {
	int input1, input2, res;

	scanf("%d %d", &input1, &input2);

	res = input1 * (input2 % 10); // 일의 자리
	printf("%d\n", res);

	printf("%d\n", input1 * (input2 % 100 / 10)); // 십의 자리
	res = res + input1 * (input2 % 100 / 10 *10) ;

	printf("%d\n", input1 * (input2 % 1000 / 100));
	res = res + input1 * (input2 % 1000 / 100 * 100);

	printf("%d\n", res);
	
	return 0;

	// 클린코드 피드백 필요 
}