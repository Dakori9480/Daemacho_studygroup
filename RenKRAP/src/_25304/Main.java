package _25304;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 영수증 (가격의 총합)
        int userInputTotal = sc.nextInt();

        // 물건의 종류 (반복 횟수)
        int userInputRep = sc.nextInt();

        // 직접 계산하는 가격의 총합
        int totalCost = 0;

        for (int i = 0; i < userInputRep; i++){

            // 물건의 가격, 물건의 갯수
            int userInputCost = sc.nextInt();
            int userInputCount = sc.nextInt();

            // 합산
            totalCost = totalCost + (userInputCost * userInputCount);
        }

        // 영수증의 가격과 동일한지 체크하는 조건문
        if (totalCost == userInputTotal) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}