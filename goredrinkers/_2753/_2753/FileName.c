#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main() {
	int input1;
	scanf("%d", &input1);
	if (input1 % 400 == 0 && input1 % 100 != 0 && input1 % 4 ==0) {
		printf("1");
	}
	else printf("0");
}