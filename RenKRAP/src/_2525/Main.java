package _2525;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInputH = sc.nextInt();
        int userInputM = sc.nextInt();
        int userInputT = sc.nextInt();
        int totalMin;
        int outHour, outMin;

        totalMin = userInputH*60 + userInputM + userInputT;
        outHour = totalMin / 60;
        outMin = totalMin % 60;
        if (outHour == 24){
            outHour = 0;
        }
        System.out.printf("%d %d", outHour, outMin);
    }
}
