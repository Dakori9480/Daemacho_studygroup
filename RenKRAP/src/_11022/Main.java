package _11022;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int userInputRepeat = Integer.parseInt(br.readLine());

        for (int i = 1; i < userInputRepeat + 1; i++){
            st = new StringTokenizer(br.readLine());
            int userInputX = Integer.parseInt(st.nextToken());
            int userInputY = Integer.parseInt(st.nextToken());

            bw.write("Case #" + i + ": " + userInputX + " + " + userInputY + " = " + (userInputX + userInputY) + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
