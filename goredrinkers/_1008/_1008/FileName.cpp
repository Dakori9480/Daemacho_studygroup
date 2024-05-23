#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    float a, b;
    scanf("%f %f", &a, &b);
    printf("%.15g", a / b);

    return 0;
}