package _10952;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        // while문에 처음 진입하기 위한 작업
        st = new StringTokenizer(br.readLine());
        int userInputX = Integer.parseInt(st.nextToken());
        int userInputY = Integer.parseInt(st.nextToken());

        // 두 입력이 모두 0이면 진입하지 않는 while문
        while ((userInputX != 0) && (userInputY != 0)) {
            // 초기 작업의 값이 0 0 이 아닐 때 실행할 작업
            bw.write((userInputX + userInputY) + "\n");

            // 토큰 배열 초기화
            st = new StringTokenizer(br.readLine());

            // 새로운 토큰 Input
            userInputX = Integer.parseInt(st.nextToken());
            userInputY = Integer.parseInt(st.nextToken());
        }
        // bw에 저장된 값 출력
        bw.flush();
        bw.close();
        br.close();

    }
}
