package _10950;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInputRep = sc.nextInt();


        for (int i = 0; i < userInputRep; i++){
            int userInput1 = sc.nextInt();
            int userInput2 = sc.nextInt();
            System.out.printf("%d\n", (userInput1+userInput2));
        }
    }
}