package _2439;


// 별 찍기 2
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int userInputRepeat = Integer.parseInt(br.readLine());

        // 전체 출력 줄 수
        for (int i = 1; i < userInputRepeat + 1; i++){
            // 띄어쓰기 갯수
            for (int k = userInputRepeat; i < k; k--){
                System.out.printf(" ");
            }

            // 별 갯수
            for (int j = 0; j < i; j++){
                System.out.printf("*");
            }
            System.out.printf("\n");
        }

    }
}
