package _8393;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int userInput = sc.nextInt();
        int forTotal = 0;

        for (int i = 0; i < userInput + 1; i++){
            forTotal = forTotal + i;
        }
        System.out.printf("%d", forTotal);
    }
}
