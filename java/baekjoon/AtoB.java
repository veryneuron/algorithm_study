package baekjoon;
import java.util.*;
import java.io.*;

// 16935

public class AtoB {
    static long target;
    static int result;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        target = B;
        result = -1;

        dfs(1, (long)A);
        System.out.println(result);
    }

    private static void dfs(int count, long current) {
        if (current == target) {
            if (result == -1 || result > count) {
                result = count;
                return;
            }
            return;
        } else if (current > target) {
            return;
        }
        dfs(count+1, current*2);
        dfs(count+1, current*10+1);
    }
}
