윤년

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int userInput = sc.nextInt(); // 사용자가 입력한 값을 변수에 저장

        if (userInput % 4 == 0 && userInput % 100 != 0){
            System.out.println(1);
        } else if (userInput % 400 == 0) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}