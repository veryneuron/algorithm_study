package baekjoon;
import java.util.*;
import java.io.*;

public class Nthnumber {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            Queue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
            while(st.hasMoreElements()) {
                pq.add(Integer.parseInt(st.nextToken()));
            }
            pq.poll();
            pq.poll();
            System.out.println(pq.poll());
        }
    }
}
