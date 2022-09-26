package baekjoon;
import java.util.*;
import java.io.*;

// 코드 참고
// 12851

public class hideAndSeek {
    static int MAX_SIZE = 100001;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] map = new int[MAX_SIZE];

        int time = 0 , count = 0;

        map[N] = 1;
        Deque<Point>dq = new ArrayDeque<>();
        dq.addLast(new Point(N, 0));

        while (!dq.isEmpty()) {
            Point now = dq.pollFirst();
            if (now.pos == K) {
                if (count == 0) {
                    time = now.time;
                }
                if (time == now.time) {
                    count++;
                }
                continue;
            }
            int[] dxList = {now.pos*2, now.pos+1, now.pos-1};
            for (var dx : dxList) {
                if (0 <= dx && dx < MAX_SIZE) {
                    if (map[dx] == 0 || map[dx] == now.time + 1) {
                        map[dx] = now.time + 1;
                        dq.addLast(new Point(dx, now.time+1));
                    }
                }
            }
        }
        System.out.println(time);
        System.out.println(count);
    }

    static class Point {
        int pos;
        int time;
        public Point(int pos, int time) {
            this.pos = pos;
            this.time = time;
        }
    }
}
