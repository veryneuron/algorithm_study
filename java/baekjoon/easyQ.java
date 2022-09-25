package baekjoon;

import java.util.*;
import java.io.*;

//1292

public class easyQ {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        List<Integer> preList = new ArrayList<>();
        for(int i = 1; i < 51; i++) {
            for(int j=0; j < i; j++) {
                preList.add(i);
            }
        }
        int answer = 0;
        for(int i = A-1; i < B; i++) {
            answer += preList.get(i);
        }
        System.out.println(answer);
    }

}
