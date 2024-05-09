#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main() {
	int a, b;
	float c;

	scanf("%d %d", &a, &b);

	c = a % b;

	printf("%lf", c);

	return 0;
	
}