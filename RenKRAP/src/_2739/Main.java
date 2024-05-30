package _2739;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInput = sc.nextInt();

        for (int i = 1; i < 10; i++){
            System.out.printf("%d * %d = %d\n", userInput, i , userInput * i);
        }
    }
}
