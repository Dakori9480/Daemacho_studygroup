#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main() {
	int input1, input2, res;

	scanf("%d %d", &input1, &input2);

	res = input1 * (input2 % 10); // ���� �ڸ�
	printf("%d\n", res);

	printf("%d\n", input1 * (input2 % 100 / 10)); // ���� �ڸ�
	res = res + input1 * (input2 % 100 / 10 *10) ;

	printf("%d\n", input1 * (input2 % 1000 / 100));
	res = res + input1 * (input2 % 1000 / 100 * 100);

	printf("%d\n", res);
	
	return 0;

	// Ŭ���ڵ� �ǵ�� �ʿ� 
}