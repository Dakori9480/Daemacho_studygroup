package _11021;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException { // 중괄호 위치 수정
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int userInputRepeat = Integer.parseInt(br.readLine());

        for (int i = 1; i < userInputRepeat + 1; i++) {
            st = new StringTokenizer(br.readLine()); // StringTokenizer 초기화
            int userInputX = Integer.parseInt(st.nextToken());
            int userInputY = Integer.parseInt(st.nextToken());
            bw.write("Case #" + i + ": "+ (userInputX + userInputY) + "\n"); // 정수 덧셈 결과와 개행 문자열로 변환하여 출력
        }
        bw.flush(); // 모든 버퍼된 출력이 출력 스트림으로 작성되도록 보장
        bw.close(); // BufferedWriter 닫기
        br.close(); // BufferedReader 닫기
    }
}
