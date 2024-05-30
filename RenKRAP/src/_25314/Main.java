package _25314;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 반복 횟수
        int userInputRepeat = sc.nextInt();

        for (int i = 0; i < userInputRepeat/4; i++) {
            System.out.printf("long ");
        }

        System.out.printf("int");
    }
}