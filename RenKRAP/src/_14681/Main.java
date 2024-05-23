package _14681;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInputX= sc.nextInt();
        int userInputY = sc.nextInt();

        if (userInputX > 0 && userInputY >0) {
            System.out.println(1);
        }
        if (userInputX < 0 && userInputY >0) {
            System.out.println(2);
        }
        if (userInputX < 0 && userInputY < 0) {
            System.out.println(3);
        }
        if (userInputX > 0 && userInputY < 0) {
            System.out.println(4);
        }
    }
}