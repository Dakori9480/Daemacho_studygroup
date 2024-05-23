package _2480;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int diceFi = sc.nextInt();
        int diceSe = sc.nextInt();
        int diceTh = sc.nextInt();
        int diceCal, diceAlldiff;

        // 같은 눈이 없는 경우
        if ((diceFi != diceSe) && (diceSe != diceTh) && (diceFi != diceTh)) {
            diceCal = (diceFi > diceSe) ? diceFi : diceSe;
            diceAlldiff = (diceTh > diceCal) ? diceTh : diceCal;

            System.out.printf("%d",diceAlldiff*100);
        }

        // 같은 눈이 2개인 경우
        int diceTwosame;
        if ((diceFi == diceSe) && (diceFi != diceTh)){
            diceTwosame = diceFi;

            System.out.printf("%d", 1000+diceTwosame*100);
        } else if ((diceFi == diceTh && diceFi != diceSe)) {
            diceTwosame = diceFi;

            System.out.printf("%d", 1000+diceTwosame*100);
        } else if ((diceSe == diceTh && diceFi != diceTh)) {
            diceTwosame = diceSe;

            System.out.printf("%d", 1000+diceTwosame*100);
        }

        // 모든 눈이 같은 경우
        if ((diceFi == diceSe) && (diceSe == diceTh)){
            System.out.printf("%d", 10000+diceFi*1000);
        }

    }
}
