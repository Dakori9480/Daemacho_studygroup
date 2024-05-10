#include <stdio.h>

int main () {
    int point;
    scanf("%d",&point);
    if (point <= 100 && point >=90){
        printf("A");
    }
    else if (point <= 89 && point >= 80){
        printf("B");
    }
    else if (point <= 79 && point >= 70){
        printf("C");
    }
    else if (point <= 69 && point >= 60){
        printf("D");
    }
    else{
        printf("F");
    }
    return 0;
}