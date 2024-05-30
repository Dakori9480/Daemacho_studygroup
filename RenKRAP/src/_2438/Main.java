package _2438;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int userInputRepeat = Integer.parseInt(br.readLine());

        for (int i = 1; i < userInputRepeat + 1; i++){
            for (int j = 0; j < i; j++){
                System.out.printf("*");
            }
            System.out.printf("\n");
        }

    }
}
