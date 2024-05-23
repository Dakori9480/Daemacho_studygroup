#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main() {
	int input1;
	scanf("%d", &input1);
	if (input1 >= 90)	printf("A");
	else if (input1 >= 80) printf("B");
	else if (input1 >= 70) printf("C");
	else if (input1 >= 60) printf("D");
	else printf("F");

}