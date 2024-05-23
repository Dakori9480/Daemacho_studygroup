package _2884;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInputH= sc.nextInt();
        int userInputM = sc.nextInt();

        if (userInputM < 45) {
            if (userInputH == 0){
                userInputH = 23;
            } else {
                userInputH = userInputH - 1;
            }
            userInputM = 15 + userInputM;
        } else {
            userInputM = userInputM - 45;
        }

        System.out.printf("%d %d", userInputH, userInputM);

    }
}