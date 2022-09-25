package baekjoon;

import java.util.*;
import java.io.*;

//1978

public class findPrime {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int count = 0;
        for(int i=0; i<N; i++) {
            if (isPrime(Integer.parseInt(st.nextToken()))) count++;
        }
        System.out.println(count);
    }

    private static Boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i < (int)Math.sqrt(num) + 1; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
