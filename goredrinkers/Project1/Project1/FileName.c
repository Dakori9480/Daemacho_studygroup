#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	long input1, input2, input3;

	scanf("%ld %ld %ld", &input1, &input2, &input3);
	printf("%ld", input1 + input2 + input3);

	return 0;
}