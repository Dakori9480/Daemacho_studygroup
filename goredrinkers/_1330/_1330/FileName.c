#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main() {
	int input1, input2;
	scanf("%d %d", &input1, &input2);
	if (input1 > input2) printf(">");
	else if (input1 < input2) printf("<");
	else printf("==");

}